from enum import Enum
from random import randint
from kafka import KafkaClient
from kafka.producer.base import Producer
from kafka.util import crc32
from ad_document_pb2 import AdDocument
from enigma_event_pb2 import EnigmaEnvelope
from ad_document_pb2 import CampaignDocument
from ad_document_pb2 import DocumentEnvelope
import logging
from mysql.connector.pooling import MySQLConnectionPool
import sys, getopt
import json
logger = logging.getLogger('kafka')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
#logger.setLevel(logging.DEBUG)

configFile= ""
APP_CONFIG = {}
APP_CONFIG["rti_kafka"] = {
        "brokers": [
           # "172.17.32.156:9092"
     #       "localhost:9092"
             # "usmv-eng-clx01.corp.xad.com:9092"
            #        "172.17.31.23:9092"
            "172.22.16.86:9092"
            ],
        "topic": "enigma.event.AdDocument",
        "partitions": 1
        }


dbconfig_marketplace = {
            "database":"marketplace",
            "user":"root",
            "port":"3336",
            "password":"venableroot",
            "host":"ec2-54-196-26-194.compute-1.amazonaws.com",
            }
dbconfig_xadcms = {
      "database":"xadcms",
      "user":"root",
      #"user":"neptune",
      "port":"3336",
      "password":"venableroot",
     # "password":"neptunexaddb",
     # "host":"ec2-52-201-178-226.compute-1.amazonaws.com",
      "host":"ec2-54-196-26-194.compute-1.amazonaws.com",
    }
class GEOType(Enum):

    NATIONAL = "national"
    STATE = "state"
    DMA = "dma"
    CITY = "city"
    ZIP = "zip"

rti_service = None
adgroupId = "0"
campaignId = "0"

def is_valid_target_profile_type(target_type):
    return target_type in set(AdDocument.TargetProfile.TargetType.values())


def is_valid_geo_target_type(target_type):
    return target_type in set(AdDocument.Geotarget.GeotargetType.values())


def add_target_profile(target_type, constraints, exclude=False):

    try:
        document = AdDocument()
        target_profile = document.target_profiles.add()
        if is_valid_target_profile_type(target_type):
            target_profile.target_type = target_type

        if isinstance(constraints, list):
            target_profile.constraints = ", ".join(constraints)
        else:
            target_profile.constraints = str(constraints)

        if exclude:
            target_profile.exclude = exclude

        return document
    except Exception as e:
        print e
        return


def add_geo_target(target_type, city_=None, state_=None, zip_=None, dma_=None, country_=None):
    try:
        document = AdDocument()
        geo_target = document.geotargets.add()

        if is_valid_geo_target_type(target_type):
            geo_target.geotarget_type = target_type

        if city_:
            geo_target.city = str(city_)

        if state_:
            geo_target.state = str(state_)

        if zip_:
            geo_target.zip = str(zip_)

        if dma_:
            geo_target.dma = str(dma_)

        if country_:
            geo_target.country = str(country_)
        return document
    except Exception as e:
        print e
        return


def make_target_profiles(rows):
    try:
        document = AdDocument()
        for row in rows:
            tp_doc = add_target_profile(row["targetType"], row["constraints"], row["exclude"])
            if tp_doc:
                document.MergeFrom(tp_doc)
        return document
    except Exception as e:
        print e
        return None


def make_geo_targets(rows):
    try:
        document = AdDocument()
        for row in rows:
            geo_type = row["geoType"].lower()
            docgeo_type = None
            if geo_type == GEOType.NATIONAL.value:
                docgeo_type = AdDocument.Geotarget.NATIONAL
            elif geo_type == GEOType.STATE.value:
                docgeo_type = AdDocument.Geotarget.STATE
            elif geo_type == GEOType.DMA.value:
                docgeo_type = AdDocument.Geotarget.DMA
            elif geo_type == GEOType.CITY.value:
                docgeo_type = AdDocument.Geotarget.CITY
            elif geo_type == GEOType.ZIP.value:
                docgeo_type = AdDocument.Geotarget.ZIP
            if docgeo_type is not None:
                geodoc = add_geo_target(docgeo_type,city_=row["city"], state_=row["state"], zip_=row["zip"], dma_=row["dma"], country_=row["country"] )
                if geodoc:
                    document.MergeFrom(geodoc)
        return document
    except Exception as e:
        print e
        return None

def make_creatives(rows):
    try:
        document = AdDocument()
        for row in rows:
            creative_doc = add_creative(row["api"], row["attributes"], row["mime"], row["video_duration"], row["video_protocol"])
            if creative_doc:
                document.MergeFrom(creative_doc)
        return document
    except Exception as e:
        print e
        return None


def add_creative(api=None,attr = None, mime = None, video_duration = None, video_protocol = None):

    try:
        document = AdDocument()
        creative = document.creatives.add()
        if api is not None:
            if  isinstance(api, list):
                creative.api = ",".join(api)
            else:
                creative.api = str(api)
        if attr is not None:
            if isinstance(attr, list):
                creative.attr = ",".join(attr)
            else:
                creative.attr = str(attr)
        if mime is not None:
            if isinstance(mime, list):
                creative.mime = ",".join(mime)
            else:
                creative.mime = str(mime)
        if video_duration is not None:
            if isinstance(video_duration, list):
                creative.video_duration = ",".join(video_duration)
            else:
                creative.video_duration = str(video_duration)
        if video_protocol is not None:
            if isinstance(video_protocol, list):
                creative.video_protocol = ",".join(video_protocol)
            else:
                creative.video_protocol = (video_protocol)

        return document
    except Exception as e:
        print e
        return None


# make_ad_document is at adgroupId Level
def make_ad_document(campaignId, adgroupId, conn):
    isAdgroupPresent = False
    try:
        document = AdDocument()
        rows = getInfoFromDB(adgroupId, sql_adgroup, conn)
        row =  None
        if rows :
            row = rows[0]

        if row is not None:
            isAdgroupPresent = True
        if isAdgroupPresent:
            document.tenant_id = row["tenant_id"] if row["tenant_id"] else 0  #1
            document.campaign_id = long(campaignId) if campaignId !="0" else long(row["campaignId"])  #2
            document.adgroup_id = long(adgroupId) if adgroupId !="0" else 0  #3
            document.adomain = "rti.com" #4   ??
                                     # 5  6  TBD
            document.banner_size = row["banner_size"] if row["banner_size"] else "" #7
            document.creative_type = row["creative_type"]  if row["creative_type"] else "" #8
            document.instl = bool(row["instl"]) if row["instl"] else False #9
            document.proximity_mode = row["proximity_mode"] if row["proximity_mode"] else ""#10
            creatives = None   #11
            target_profiles = None  #12
            geo_targets = None  #13
            publishers = None  #14
            document.status = row["status_flag"] if row["status_flag"] else 6#15
            setattr(document,'del',bool(row["del"]))#16
            document.rti_mode = AdDocument.BATCH   #17
            document.adv_bid_rates = row["bid_rate"] if row["bid_rate"] else 0.0#18
            document.is_secure = bool( row["is_secure"]) if row["is_secure"] else False #19
            document.session_id = randint(0,1000000)    #20
            document.pub_bid_rates = 0.0    #21
            document.kpi_ctr = row["kpi_ctr"] if row["kpi_ctr"] else 0.0 #22
            document.kpi_sar = row["kpi_sar"] if row["kpi_sar"] else 0.0 #23
                                           #24  TBD

        if isAdgroupPresent:
            #get targetprofile info from db
            targetprofiles_rows = getInfoFromDB(adgroupId, sql_targetprofiles, conn)
            if targetprofiles_rows:
                target_profiles = make_target_profiles(targetprofiles_rows)

            if target_profiles:
                document.MergeFrom(target_profiles)

            #get geotarget info from db
            geotargets_rows = getInfoFromDB(adgroupId, sql_geotargets, conn)
            '''
            conn_marketplace = getConnectWithDB(dbconfig_marketplace, "marketplace_pool")
            if geotargets_rows:
                insert_rows = []
                for row in geotargets_rows:
                    if row["lat"] and row["lng"] and row["radius"]:
                        data = {
                                "id" : row["gtId"],
                                "tenant_id" : row["tenant_id"],
                                "study_id" : document.session_id,
                                "address1" :  row["address1"] ,
                                "address2":   row["address2"],
                                "city":      row["city"],
                                "state":      row["state"],
                                "country":     row["country"],
                                "zipcode":      row["zip"] ,
                                "latittude":      row["lat"],
                                "longitude":      row["lng"],
                                "type":      row["geoType"],
                                "adgroup":      row["adGroup_id"],
                                "dma_code":      row["dma"],
                                "radius":      row["radius"]
                                }
                        insert_rows.append((
                                      (row["gtId"]),
                                      (row["tenant_id"]),
                                      (document.session_id),
                                      (row["address1"]) ,
                                      (row["address2"]),
                                      (row["city"]),
                                      (row["state"]),
                                      (row["country"]),
                                      (row["zip"]) ,
                                      (row["lat"]),
                                      (row["lng"]),
                                      (row["geoType"]),
                                      (row["adGroup_id"]),
                                      (row["dma"]),
                                      (row["radius"])
                                    ))
                insertInfoToDB(insert_rows, conn_marketplace)
            '''
            if geotargets_rows:
                geo_targets = make_geo_targets(geotargets_rows)
            if geo_targets:
                document.MergeFrom(geo_targets)
            #closeDB(conn_marketplace)
            #get creative info from db
            creative_rows = getInfoFromDB(adgroupId, sql_creatives, conn)
            if creative_rows:
                creatives = make_creatives(creative_rows)
            if creatives:
                document.MergeFrom(creatives)
        print document  # for final test when sending
        return document
    except Exception as e:
        print e
        return None


def make_enigma_envelope(topic, data, heartbeat=False):
    try:
        envelope = EnigmaEnvelope()
        envelope.event_topic = topic
        envelope.event_data = data
        envelope.is_heartbeat = heartbeat
        return envelope.SerializeToString()
    except Exception as e:
        return None

def make_document_envelope(level, data):
    try:
        envelope = DocumentEnvelope()
        envelope.doc_level= level
        envelope.doc_data = data
        return envelope.SerializeToString()
    except Exception as e:
        print e
        return None

def make_campaign_document(addocs):
    try:
        document = CampaignDocument()
        for addoc in addocs:
            doc = document.ad_docs.add()
            doc.MergeFrom(addoc)
        print document.SerializeToString()
        return document.SerializeToString()
    except Exception as e:
        print e
        return None

class RTIProducer(Producer):

    def __init__(self, *args, **kwargs):
        super(RTIProducer, self).__init__(*args, **kwargs)

    def send_messages(self, topic, partition, *msg):
        if not isinstance(topic, str):
            topic = topic.encode("utf-8")

        if not isinstance(partition, (int, long)):
            raise

        return super(RTIProducer, self).send_messages(topic, partition, *msg)

    def __repr__(self):
        return '<RTIProducer batch=%s>' % self.async

class RTIService(object):

    def __init__(self):
        self._brokers = APP_CONFIG["rti_kafka"]["brokers"]
        self._partitions = APP_CONFIG["rti_kafka"]["partitions"]
        self._topic = APP_CONFIG["rti_kafka"]["topic"]
        self._kafka = KafkaClient(self._brokers)
        self.producer = None

    def close(self):
        self._kafka.close()

    def connect(self):
        if not self.producer:
            self.producer = RTIProducer(self._kafka)

    def emit_event(self, adgroupId, campaignId):
        adDocs = []
        conn = getConnectWithDB(dbconfig_xadcms, "xadcms_pool")
        if adgroupId !="0" :
            document = make_ad_document(campaignId, adgroupId, conn)
            adDocs.append(document)
       # campaign level
        elif  campaignId != "0"  :
            #get adgroupIds for this campaign
            adgroupIdRows = getInfoFromDB(campaignId, sql_campaign_adgroups, conn)
            print "c level"
            for row in adgroupIdRows:
                document =  make_ad_document(campaignId, row["adgroupId"], conn)
                adDocs.append(document)
        campaignDoc = make_campaign_document(adDocs)
        closeDB(conn)
        envelope = make_document_envelope(1,campaignDoc)
        message = make_enigma_envelope(self._topic, envelope)
        totalPartitions = self._partitions
        partition  = randint(0,totalPartitions - 1)

        try:
            response = self.producer.send_messages(self._topic, partition, message)
            print response
        except Exception as e:
            return
            print(e)



def start_rti_service():
    global rti_service
    try:
        rti_service = RTIService()
        print(rti_service)
    except:
        pass


def stop_rti_service():
    global rti_service
    if rti_service:
        rti_service.close()

def dbconfigload(db_name, user_name, port, password, host_name, pool_name):
        dbconfig = {}
        dbconfig["database"] = db_name
        dbconfig["user"] = user_name
        dbconfig["port"] = port
        dbconfig["password"] = password
        dbconfig["host"] = host_name
        return MySQLConnectionPool(pool_name = pool_name,
                               pool_size = 3,
                                **dbconfig)

'''
        dbconfig = {
            "database":"marketplace",
            "user":"root",
            "port":"3336",
            "password":"venableroot",
            "host":"ec2-54-196-26-194.compute-1.amazonaws.com"
               }
'''
def create_mysql_pool(dbconfig, pool_name):
        return MySQLConnectionPool(pool_name = pool_name,
                               pool_size = 3,
                                **dbconfig)

# sql for multiple tables

sql_targetprofiles = '''
    SELECT
        tp.adGroup_id adGroup_id,
        tp.targetType targetType,
        tp.exclude exclude,
        GROUP_CONCAT(DISTINCT tp.constraints)  as constraints
    FROM targetprofile tp
    WHERE tp.adGroup_id = %(Id)s
    GROUP BY tp.targetType
                    '''
sql_geotargets = '''
    SELECT
        gt.tenant_id tenant_id,
        gt.id gtId,
        gt.adGroup_id adGroup_id,
        gt.address1  address1,
        gt.address2  address2,
        gt.lat  lat,
        gt.lng  lng,
        gt.type geoType,
        gt.dma dma,
        gt.city city,
        gt.state state,
        gt.zipcode  zip,
        gt.country country,
        gt.radius  radius
    FROM geotarget gt
    WHERE gt.adGroup_id = %(Id)s
                '''
sql_creatives = '''
    SELECT
        c.api  api
       , c.name attributes
       , c.mimeType  mime
       , c.videoDuration video_duration
       , c.videoProtocol video_protocol
    FROM creative c
    WHERE c.adGroup_id = %(Id)s and c.del != 1

            '''
sql_campaign_adgroups = '''
    SELECT
        adg.campaign_id  campaignId,
        adg.id  as adgroupId
    FROM adgroup adg
    WHERE adg.campaign_id = %(Id)s and adg.del != 1
             '''
sql_adgroup = '''
    SELECT
        tenant_id,
        adg.campaign_id campaignId,
        adg.size banner_size,
        adg.interstitial  instl,
        adg.proximity_mode proximity_mode,
        adg.status status_flag,
        adg.del  del,
        adg.type creative_type,
        adg.bidRates bid_rate,
        adg.is_secure is_secure,
        adg.ctr_threshold kpi_ctr,
        adg.sar_threshold kpi_sar
from adgroup adg
where adg.id = %(Id)s
               '''
sql_insert_mp_geotarget = """
                    INSERT INTO geotargetstest
                    (
                     id,
                     tenant_id,
                     study_id,
                     address1,
                     address2,
                     city,
                     state,
                     country,
                     zipcode,
                     latitude,
                     longitude,
                     type,
                     adgroup,
                     dma_code,
                     radius
                    )
                    values
                    (
                      %s,
                      %s,
                      %s,
                      %s,
                      %s,
                      %s,
                      %s,
                      %s,
                      %s,
                      %s,
                      %s,
                      %s,
                      %s,
                      %s,
                      %s
                    )
                         """
                    #ON DUPLICATE KEY UPDATE id = %s
sql_clean = '''
            delete from geotargetstest  where adgroup = %s
            '''
def getConnectWithDB(dbconfig, pool_name):
    mysql_pool = create_mysql_pool(dbconfig, pool_name)
    conn = mysql_pool.get_connection()
    return conn

def getInfoFromDB(Id, query, conn):
    cursor = conn.cursor(dictionary=True,buffered=True)
    try:
        params ={'Id':Id}
        cursor.execute(query, params)
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
        raise
    finally:
        cursor.close()
        return rows

def closeDB(conn):
    conn.close()

def insertInfoToDB(data, conn):
    try:
        cursor = conn.cursor(dictionary=True,buffered=True)
        cursor.executemany(sql_insert_mp_geotarget, data)
        conn.commit()
    except Exception as e:
        print(e)
        raise
    finally:
        cursor.close()

def process_argument(argv):
    try:
        opts, args = getopt.getopt(argv,"ha:c:j:",["adgroupId=","campaignId=", "configFile="])
    except getopt.GetoptError:
        print 'rti.py -a <adgroupId> or rti.py -c <campaignId>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'rti.py -a <adgroupId> or rti.py -c <campaignId>'
            sys.exit()
        elif opt == '-a':
            global adgroupId
            adgroupId = arg
        elif opt == '-c':
            global campaignId
            campaignId = arg
        elif opt == '-j':
            global dbConfigFile
            configFile = arg
    with open(configFile) as data_file:
        data = json.load(data_file)
    populatedbconfig(data)
    print "adgroup:" + adgroupId + "campaignId: "+campaignId + "dbconfiFile:" + configFile

def populatedbconfig(data):
    global dbconfig_xadcms
    global dbconfig_marketplace
    dbconfig_xadcms["database"] = "xadcms"
    dbconfig_xadcms["user"] = data ["user"]
    dbconfig_xadcms["port"] = data ["port"]
    dbconfig_xadcms["password"] = data ["password"]
    dbconfig_xadcms["host"] = data ["host"]

    dbconfig_marketplace["database"] = "marketplace"
    dbconfig_marketplace["user"] = data["user"]
    dbconfig_marketplace["port"] = data["port"]
    dbconfig_marketplace["password"] = data["password"]
    dbconfig_marketplace["host"] = data["host"]

def main(argv):
    process_argument(argv)

    rti_service = RTIService()
    if rti_service:
        rti_service.connect()
        rti_service.emit_event( adgroupId, campaignId)
if __name__ == "__main__":
    main(sys.argv[1:])
