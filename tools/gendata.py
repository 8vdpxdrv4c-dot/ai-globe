import json
US=json.load(open('/tmp/oldUS.json'))
US# 光刻胶材料 / 涂胶显影·光刻设备（中日）
A('JK',[["jsr-yk", "JSR 四日市", "JSR Yokkaichi", "日本 三重 四日市", 34.96, 136.62, "mat", "JSR 主力工厂，光刻胶生产与精细电子材料研发中心（EUV/MOR 光刻胶开发）。", "光刻胶"], ["tok", "东京应化", "TOK", "日本 神奈川 川崎", 35.575, 139.66, "mat", "全球光刻胶龙头之一，总部川崎；主要产线在寒川、郡山、宇都宫、御殿场、阿苏等地。", "光刻胶"], ["shinetsu-nt", "信越化学 直江津", "Shin-Etsu Naoetsu", "日本 新潟 上越", 37.17, 138.24, "mat", "信越光刻胶起点工厂（1997 年起量产 KrF），ArF/EUV 光刻胶与多层材料。", "光刻胶"], ["sumi", "住友化学 大阪", "Sumitomo Chemical Osaka", "日本 大阪", 34.68, 135.44, "mat", "大阪工厂（此花区）为光刻胶核心基地，ArF 浸没式份额领先并扩产 EUV 胶；总部东京/大阪。", "光刻胶"], ["ffem", "富士胶片电子材料", "Fujifilm Electronic Materials", "日本 静冈 吉田", 34.77, 138.25, "mat", "静冈工厂生产先进光刻胶（含 EUV），2025 年新建研发评估楼投产。", "光刻胶"], ["tel-ks", "东京电子九州", "TEL Kyushu", "日本 熊本 合志", 32.89, 130.77, "equip", "涂胶显影设备研发制造基地，全球涂胶显影龙头，EUV 线份额近乎独占。", "涂胶显影/光刻"], ["screen", "SCREEN", "SCREEN Holdings", "日本 京都", 35.03, 135.75, "equip", "总部京都，晶圆清洗设备龙头，同时提供涂胶显影设备。", "涂胶显影/光刻"], ["nikon", "尼康 熊谷", "Nikon Kumagaya", "日本 埼玉 熊谷", 36.17, 139.37, "equip", "光刻机开发、测试与量产工厂（总部东京品川）。", "涂胶显影/光刻"], ["canon", "佳能 宇都宫", "Canon Utsunomiya", "日本 栃木 宇都宫", 36.55, 139.95, "equip", "光刻机设计与生产（宇都宫光学工厂），i 线光刻机全球份额第一。", "涂胶显影/光刻"]])
A('CN',[["rdav", "彤程新材", "Red Avenue", "上海", 31.23, 121.47, "mat", "国内半导体与显示面板光刻胶龙头之一，总部上海，上海化工区建设光刻胶项目。", "光刻胶"], ["bjkh", "北京科华", "Kempur (Red Avenue)", "北京", 39.95, 116.35, "mat", "彤程新材控股子公司，G/I 线、KrF、ArF 光刻胶，供应中芯国际、长江存储、华虹等。", "光刻胶"], ["nata", "南大光电 宁波", "NATA Ningbo", "浙江 宁波 北仑", 29.87, 121.84, "mat", "宁波南大光电负责 ArF 光刻胶研发与产业化（母公司总部苏州工业园区）。", "光刻胶"], ["jingrui", "晶瑞电材", "Jingrui", "江苏 苏州", 31.27, 120.62, "mat", "子公司苏州瑞红生产 g/i 线、KrF 半导体光刻胶及面板光刻胶。", "光刻胶"], ["sinyang", "上海新阳", "Sinyang", "上海", 31.2, 121.38, "mat", "I 线、KrF、ArF 干法及浸没式光刻胶，兼营电镀液与清洗液。", "光刻胶"], ["bokang", "徐州博康", "Bokang", "江苏 徐州", 34.26, 117.18, "mat", "光刻胶单体-树脂-光刻胶全链条，ArF/KrF 单体全球份额超两成。", "光刻胶"], ["hengkun", "恒坤新材", "Hengkun", "福建 厦门", 24.49, 118.03, "mat", "12 英寸 SOC、BARC、KrF/i 线光刻材料，ArF 浸没式胶已小批量销售。", "光刻胶"], ["rongda", "容大感光", "Rongda", "广东 深圳", 22.7, 113.95, "mat", "PCB 与显示光刻胶为主，拓展 g/i 线半导体光刻胶。", "光刻胶"], ["qiangli", "强力新材", "Tronly", "江苏 常州", 31.78, 119.95, "mat", "光刻胶专用光引发剂与树脂等上游原料。", "光刻胶"], ["byss", "八亿时空", "Bayi Space", "北京", 39.73, 116.14, "mat", "面板 PSPI 光刻胶与 KrF 光刻胶树脂。", "光刻胶"], ["kingsemi", "芯源微", "Kingsemi", "辽宁 沈阳", 41.74, 123.43, "equip", "国产前道涂胶显影设备龙头，覆盖 I-line/KrF/ArF 浸没式，28nm 及以上。", "涂胶显影/光刻"], ["uprec", "华卓精科", "U-Precision", "北京", 40.04, 116.3, "equip", "光刻机双工件台与超精密运动系统。", "涂胶显影/光刻"]])
PR_TAGS={"tel": "涂胶显影/光刻", "smee": "涂胶显影/光刻", "shinetsu": "光刻胶", "jsr": "光刻胶"}
PR_DESC={"shinetsu": "全球最大硅片与光刻胶供应商之一；光刻胶产线见直江津（另有福井、云林、伊势崎基地）。", "tel": "涂胶显影/刻蚀/沉积设备；涂胶显影在熊本合志（东京电子九州）研制。"}
for r in S:
    if r[0] in PR_DESC: r[8]=PR_DESC[r[0]]
    if r[0] in PR_TAGS: r[9:]=[PR_TAGS[r[0]]]
SEG={'nvda':'design','amd':'design','intc':'design','mrvl':'design','amat':'equip','anet':'net','avgo':'design','snps':'eda','cdns':'eda','smci':'server','lite':'optic','csco':'net','lrcx':'equip','klac':'equip','aapl':'device','qcom':'design','intc-or':'foundry','mu':'mem','mu-ny':'mem','mu-va':'mem','tsmc-az':'foundry','intc-az':'foundry','intc-nm':'pkg','txn':'foundry','ssg':'foundry','ssg-t':'foundry','dell':'server','hpe':'server','skh':'pkg','vrt':'power','gfs':'foundry','cohr':'optic','ter':'equip','adi':'design','gev':'power','hubb':'power','aws':'cloud','msft':'cloud','goog-or':'dc','meta-or':'dc','aws-or':'dc','goog-ia':'dc','meta-ia':'dc','aws-oh':'dc','meta-oh':'dc','stargate':'dc','crwv':'cloud','aws-va':'dc','hq2':'cloud','oai':'model','anth':'model','dbx':'data','meta':'model','goog':'model','ibm':'ent','crm':'ent','now':'ent','adbe':'ent','isrg':'med','figure':'robot','waymo':'auto','rxrx':'med','de':'ind','rok':'ind','gm':'auto','tem':'med','pltr':'data','pltr-fl':'data','tsla':'auto','anduril':'def','aur':'auto','path':'ent','bd':'robot','amzr':'robot','cgnx':'ind'}
S=[]
for d in US:
    id,cn,en,city,lat,lon,layer,cty,role,desc=d
    S.append([id,cn,en,city,lat,lon,USSEG[id],'US',desc])
def A(region,rows):
    for r in rows: S.append([r[0],r[1],r[2],r[3],r[4],r[5],r[6],region,r[7]]+list(r[8:]))
A('US',[
['glw','康宁','Corning','纽约州 康宁',42.143,-77.055,'optic','光纤与光缆龙头，AI 数据中心高密度光纤连接主要供应商。'],
['ttm','TTM 科技','TTM Technologies','加州 圣安娜',33.745,-117.868,'pcb','美国最大 PCB 制造商之一，服务器与国防高多层板。'],
['aph','安费诺','Amphenol','康涅狄格 沃灵福德',41.457,-72.823,'net','连接器与高速铜缆，NVLink 机柜背板互连核心供应商。'],
['jbl','捷普','Jabil','佛罗里达 圣彼得堡',27.877,-82.645,'server','EMS 代工，数据中心基础设施与光模块制造。'],
['amkor-az','安靠 亚利桑那','Amkor Arizona','亚利桑那 皮奥里亚',33.66,-112.33,'pkg','在建先进封装厂，承接台积电亚利桑那 CoWoS 等后段。'],
['xai','xAI Colossus','xAI Colossus','田纳西 孟菲斯',35.06,-90.03,'dc','xAI 超大规模 GPU 训练集群 Colossus。'],
['orcl','甲骨文','Oracle','得州 奥斯汀',30.24,-97.72,'cloud','OCI 云，Stargate 合作方，总部奥斯汀。'],
['lambda','Lambda','Lambda','加州 圣何塞',37.34,-121.89,'cloud','GPU 云服务商。'],
['scale','Scale AI','Scale AI','加州 旧金山',37.776,-122.42,'data','AI 训练数据标注与评测平台。'],
['snow','Snowflake','Snowflake','蒙大拿 博兹曼',45.68,-111.04,'data','云数据平台（行政总部博兹曼）。'],
['wolf','Wolfspeed','Wolfspeed','北卡 达勒姆',35.99,-78.90,'mat','碳化硅衬底与功率器件。'],
['entg','英特格','Entegris','马萨诸塞 比勒里卡',42.56,-71.27,'mat','半导体特种化学品、过滤与材料。'],
['eaton','伊顿','Eaton','俄亥俄 克利夫兰(美国总部)',41.50,-81.69,'power','配电与 UPS，数据中心电力设备。'],
])
A('CN',[
# 芯片设计
['hisi','华为海思 / 昇腾','HiSilicon / Ascend','广东 深圳',22.657,114.058,'design','昇腾 910 系列 AI 芯片与鲲鹏 CPU，国产算力核心。'],
['camb','寒武纪','Cambricon','北京',39.98,116.33,'design','思元系列云端 AI 芯片。'],
['hygon','海光信息','Hygon','天津',39.084,117.20,'design','海光 x86 CPU 与深算 DCU。'],
['mthreads','摩尔线程','Moore Threads','北京',39.91,116.46,'design','全功能 GPU 与 MUSA 架构。'],
['metax','沐曦','MetaX','上海',31.20,121.60,'design','曦云系列 GPGPU（总部上海浦东）。'],
['biren','壁仞科技','Biren','上海',31.19,121.44,'design','BR 系列通用 GPU。'],
['enflame','燧原科技','Enflame','上海',31.18,121.46,'design','云端 AI 训练/推理芯片。'],
['thead','平头哥','T-Head','浙江 杭州',30.28,120.02,'design','阿里旗下芯片公司，含光 AI 芯片与玄铁 RISC-V。'],
['kunlun','昆仑芯','Kunlunxin','北京',40.05,116.30,'design','百度孵化 AI 芯片。'],
['ilu','天数智芯','Iluvatar CoreX','上海',31.21,121.55,'design','通用 GPU。'],
['loongson','龙芯中科','Loongson','北京',40.03,116.27,'design','自主 CPU 架构 LoongArch。'],
['empyrean','华大九天','Empyrean','北京',39.98,116.31,'eda','国产 EDA 龙头。'],
# 设备
['naura','北方华创','NAURA','北京',39.79,116.51,'equip','刻蚀/沉积/清洗等设备平台型龙头（亦庄）。'],
['amec','中微公司','AMEC','上海',31.20,121.62,'equip','等离子刻蚀与 MOCVD 设备。'],
['smee','上海微电子','SMEE','上海',31.19,121.60,'equip','国产光刻机研发制造（张江）。'],
['piotech','拓荆科技','Piotech','辽宁 沈阳',41.80,123.43,'equip','PECVD/ALD 薄膜沉积设备。'],
['acmr','盛美上海','ACM Research Shanghai','上海',31.10,121.60,'equip','清洗与电镀设备。'],
# 材料
['nsig','沪硅产业','NSIG','上海',30.90,121.90,'mat','300mm 大硅片（临港）。'],
['anji','安集科技','Anji Micro','上海',31.20,121.61,'mat','CMP 抛光液与功能湿化学品。'],
['jcet-mat','江丰电子','KFMI','浙江 宁波 余姚',30.04,121.15,'mat','超高纯溅射靶材。'],
# 代工
['smic','中芯国际 上海','SMIC Shanghai','上海',31.205,121.60,'foundry','中国大陆最大晶圆代工厂，先进制程主力。'],
['smic-bj','中芯国际 北京','SMIC Beijing','北京 亦庄',39.80,116.52,'foundry','12 英寸晶圆厂（中芯北方/京城）。'],
['smic-sz','中芯国际 深圳','SMIC Shenzhen','广东 深圳',22.63,114.08,'foundry','12 英寸晶圆项目。'],
['smic-tj','中芯国际 天津','SMIC Tianjin','天津',39.12,117.32,'foundry','12 英寸晶圆厂。'],
['hua','华虹集团','Hua Hong','上海',31.21,121.58,'foundry','特色工艺代工（另有无锡 12 英寸厂）。'],
['hua-wx','华虹 无锡','Hua Hong Wuxi','江苏 无锡',31.49,120.37,'foundry','华虹 12 英寸 Fab7/Fab9。'],
# 存储
['cxmt','长鑫存储','CXMT','安徽 合肥',31.82,117.23,'mem','国产 DRAM 龙头，推进 HBM。'],
['ymtc','长江存储','YMTC','湖北 武汉',30.46,114.42,'mem','Xtacking 3D NAND。'],
# 封测
['jcet','长电科技','JCET','江苏 江阴',31.91,120.28,'pkg','全球前三封测，XDFOI 先进封装。'],
['tfme','通富微电','TFME','江苏 南通',32.03,120.86,'pkg','AMD 主要封测伙伴。'],
['hts','华天科技','Huatian','甘肃 天水',34.58,105.72,'pkg','封测龙头之一（另有西安/昆山基地）。'],
# PCB
['victory','胜宏科技','Victory Giant','广东 惠州',23.11,114.42,'pcb','AI 服务器/GPU 加速卡高多层 PCB 核心供应商。'],
['wus','沪电股份','WUS Printed Circuit','江苏 昆山',31.39,120.98,'pcb','数据中心交换机/服务器高速 PCB。'],
['scc','深南电路','Shennan Circuits','广东 深圳',22.67,113.95,'pcb','PCB 与 IC 封装基板。'],
['kinwong','景旺电子','Kinwong','广东 深圳',22.72,113.83,'pcb','多品类 PCB。'],
['zdt','鹏鼎控股','ZDT (Avary)','广东 深圳',22.66,113.90,'pcb','全球最大 PCB 厂商之一。'],
['sytech','生益科技','Shengyi Tech','广东 东莞',23.02,113.75,'pcb','高速覆铜板（PCB 基材）。'],
# 光模块
['innolight','中际旭创','InnoLight','山东 龙口',37.65,120.48,'optic','全球 800G/1.6T 光模块龙头，英伟达/北美云厂商核心供应商（上市主体在龙口）。'],
['innolight-sz','中际旭创 苏州','InnoLight Suzhou','江苏 苏州',31.30,120.70,'optic','苏州旭创——光模块主要研发制造基地。'],
['eoptolink','新易盛','Eoptolink','四川 成都',30.60,104.05,'optic','高速光模块，海外客户占比超九成。'],
['tfc','天孚通信','TFC Optical','江苏 苏州',31.32,120.62,'optic','光器件/光引擎，CPO 配套。'],
['accelink','光迅科技','Accelink','湖北 武汉',30.50,114.40,'optic','光芯片到光模块垂直整合。'],
['hgg','华工正源','HG Genuine','湖北 武汉',30.49,114.43,'optic','华工科技旗下光模块。'],
['yj','源杰科技','Yuanjie','陕西 西安',34.20,108.86,'optic','光芯片（CW 光源/DFB）IDM。'],
# 服务器
['inspur','浪潮信息','Inspur','山东 济南',36.67,117.12,'server','中国最大 AI 服务器厂商。'],
['fii','工业富联','Foxconn Industrial Internet','广东 深圳',22.65,114.02,'server','全球 AI 服务器/GB200 机柜主要代工方。'],
['sugon','中科曙光','Sugon','北京',40.05,116.28,'server','高性能计算与液冷数据中心。'],
['huaqin','华勤技术','Huaqin','上海',31.20,121.58,'server','ODM，数据中心服务器业务快速增长（总部张江）。'],
['h3c','新华三','H3C','浙江 杭州',30.21,120.21,'net','服务器与网络设备（紫光旗下）。'],
['ruijie','锐捷网络','Ruijie','福建 福州',26.08,119.30,'net','数据中心交换机。'],
['zte','中兴通讯','ZTE','广东 深圳',22.54,113.95,'net','服务器、交换机与通信设备。'],
# 电源液冷
['envicool','英维克','Envicool','广东 深圳',22.70,114.10,'power','数据中心精密温控与液冷。'],
['megmeet','麦格米特','Megmeet','广东 深圳',22.55,113.93,'power','服务器电源。'],
['kehua','科华数据','Kehua','福建 厦门',24.48,118.10,'power','UPS 与数据中心电力。'],
# 中游 数据中心 8 枢纽
['dc-zjk','京津冀枢纽 张家口','Zhangjiakou Hub','河北 张家口',40.82,114.88,'dc','东数西算京津冀枢纽（张家口集群）。'],
['dc-csj','长三角枢纽 芜湖','Wuhu Hub','安徽 芜湖',31.33,118.43,'dc','东数西算长三角枢纽芜湖集群。'],
['dc-qy','粤港澳枢纽 韶关','Shaoguan Hub','广东 韶关',24.81,113.60,'dc','东数西算粤港澳枢纽韶关集群。'],
['dc-cy','成渝枢纽 天府','Tianfu Hub','四川 成都 天府',30.40,104.07,'dc','东数西算成渝枢纽（天府/重庆集群）。'],
['dc-nm','内蒙古枢纽 和林格尔','Horinger Hub','内蒙古 和林格尔',40.38,111.82,'dc','东数西算内蒙古枢纽。'],
['dc-wlcb','乌兰察布数据中心','Ulanqab DCs','内蒙古 乌兰察布',41.00,113.13,'dc','阿里、华为等大型数据中心。'],
['dc-gz','贵州枢纽 贵安','Gui\'an Hub','贵州 贵安',26.42,106.46,'dc','东数西算贵州枢纽，华为云、腾讯、苹果数据中心。'],
['dc-gs','甘肃枢纽 庆阳','Qingyang Hub','甘肃 庆阳',35.71,107.64,'dc','东数西算甘肃枢纽庆阳集群。'],
['dc-nx','宁夏枢纽 中卫','Zhongwei Hub','宁夏 中卫',37.51,105.19,'dc','东数西算宁夏枢纽，AWS、美团等。'],
# 云
['ali','阿里云 / 通义千问','Alibaba Cloud / Qwen','浙江 杭州',30.28,120.02,'cloud','中国最大云厂商，Qwen 开源模型。'],
['tc','腾讯云 / 混元','Tencent Cloud','广东 深圳',22.54,113.935,'cloud','腾讯云与混元大模型。'],
['volc','字节 火山引擎 / 豆包','ByteDance Volcano / Doubao','北京',39.96,116.30,'cloud','豆包大模型与火山引擎。'],
['hwc','华为云','Huawei Cloud','贵州 贵安',26.42,106.46,'cloud','华为云全球总部落户贵安。'],
['bidu','百度智能云 / 文心','Baidu ERNIE','北京',40.05,116.30,'model','文心大模型。'],
['ds','深度求索','DeepSeek','浙江 杭州',30.25,120.17,'model','DeepSeek-V3/R1 开源模型。'],
['kimi','月之暗面','Moonshot AI','北京',39.99,116.31,'model','Kimi 大模型。'],
['zhipu','智谱','Zhipu AI','北京',40.00,116.33,'model','GLM 系列。'],
['minimax','MiniMax','MiniMax','上海',31.23,121.47,'model','多模态与视频生成。'],
['step','阶跃星辰','StepFun','上海',31.22,121.53,'model','Step 系列多模态。'],
['sense','商汤科技','SenseTime','上海',31.17,121.39,'model','日日新大模型与 AI 大装置。'],
['iflytek','科大讯飞','iFlytek','安徽 合肥',31.83,117.14,'model','讯飞星火大模型。'],
['baichuan','百川智能','Baichuan','北京',39.98,116.32,'model','百川大模型。'],
# 下游
['unitree','宇树科技','Unitree','浙江 杭州',30.19,120.19,'robot','四足与人形机器人。'],
['ubtech','优必选','UBTech','广东 深圳',22.59,113.99,'robot','Walker 工业人形机器人。'],
['agibot','智元机器人','AgiBot','上海',31.28,121.17,'robot','通用人形机器人（临港/嘉定）。'],
['galbot','银河通用','Galbot','北京',40.04,116.29,'robot','具身智能机器人。'],
['dji','大疆','DJI','广东 深圳',22.58,113.95,'device','无人机与智能影像。'],
['xiaomi','小米','Xiaomi','北京',40.03,116.31,'device','手机/AIoT 与小米汽车。'],
['byd','比亚迪','BYD','广东 深圳',22.69,114.35,'auto','智能电动车，天神之眼智驾。'],
['horizon','地平线','Horizon Robotics','北京',40.04,116.27,'auto','征程智驾芯片。'],
['apollo','百度 Apollo','Baidu Apollo','北京 亦庄',39.79,116.50,'auto','萝卜快跑无人驾驶。'],
['pony','小马智行','Pony.ai','广东 广州',23.13,113.37,'auto','Robotaxi。'],
['weride','文远知行','WeRide','广东 广州',23.16,113.43,'auto','自动驾驶。'],
['xpeng','小鹏汽车','XPeng','广东 广州',23.15,113.30,'auto','智能电动车与人形机器人。'],
['nio','蔚来','NIO','安徽 合肥',31.80,117.20,'auto','智能电动车。'],
['li','理想汽车','Li Auto','北京',40.06,116.40,'auto','智能电动车。'],
['catl','宁德时代','CATL','福建 宁德',26.66,119.55,'ind','动力与储能电池（数据中心储能）。'],
['kingsoft','金山办公','Kingsoft Office','北京',40.04,116.30,'ent','WPS AI 办公。'],
['yonyou','用友网络','Yonyou','北京',40.07,116.24,'ent','企业软件与 AI。'],
['united-imaging','联影医疗','United Imaging','上海',31.30,121.25,'med','医学影像与 AI 诊断（嘉定）。'],
['hik','海康威视','Hikvision','浙江 杭州',30.21,120.21,'ind','视觉感知与工业 AI。'],
['luxshare','立讯精密','Luxshare','广东 东莞',22.97,113.73,'net','高速铜连接/电源/光模块，GB200 铜缆供应商。'],
])
A('TW',[
['tsmc-hc','台积电 新竹','TSMC Hsinchu','中国台湾 新竹',24.78,120.998,'foundry','台积电总部与研发、先进制程。'],
['tsmc-tc','台积电 台中','TSMC Taichung','中国台湾 台中',24.21,120.62,'foundry','Fab 15 及先进封装厂。'],
['tsmc-tn','台积电 台南','TSMC Tainan','中国台湾 台南',23.11,120.27,'foundry','南科 Fab 18（3nm/5nm）。'],
['tsmc-ks','台积电 高雄','TSMC Kaohsiung','中国台湾 高雄',22.73,120.32,'foundry','Fab 22（2nm）。'],
['tsmc-cowos','台积电 CoWoS 竹南/嘉义','TSMC AP6/AP7','中国台湾 竹南',24.68,120.87,'pkg','CoWoS 先进封装主力产能（另有嘉义 AP7）。'],
['ase','日月光 ASE','ASE','中国台湾 高雄',22.72,120.30,'pkg','全球最大封测厂（楠梓）。'],
['spil','矽品 SPIL','SPIL','中国台湾 台中',24.25,120.60,'pkg','日月光旗下封测。'],
['hh','鸿海 / 富士康','Foxconn','中国台湾 新北 土城',24.97,121.44,'server','全球最大电子代工，AI 服务器机柜龙头。'],
['quanta','广达','Quanta','中国台湾 桃园 龟山',25.05,121.36,'server','云服务器 ODM，GB200 主要组装商。'],
['wistron','纬创','Wistron','中国台湾 新北 汐止',25.07,121.66,'server','GPU 基板与服务器 ODM。'],
['wiwynn','纬颖','Wiwynn','中国台湾 新北',25.06,121.65,'server','超大规模云服务器 ODM。'],
['inventec','英业达','Inventec','中国台湾 台北',25.08,121.57,'server','服务器 ODM。'],
['delta','台达电','Delta Electronics','中国台湾 台北',25.07,121.57,'power','服务器电源与液冷，数据中心电力龙头。'],
['mtk','联发科','MediaTek','中国台湾 新竹',24.785,121.01,'design','芯片设计，参与定制 AI ASIC。'],
['unimicron','欣兴电子','Unimicron','中国台湾 桃园',24.99,121.30,'pcb','ABF 载板龙头。'],
['nya','南亚电路板','Nan Ya PCB','中国台湾 桃园 芦竹',25.05,121.29,'pcb','ABF 载板。'],
['accton','智邦','Accton','中国台湾 新竹',24.78,121.02,'net','白牌数据中心交换机（AI 以太网）。'],
['umc','联电','UMC','中国台湾 新竹',24.77,121.00,'foundry','成熟制程代工。'],
['gudeng','台光电子','EMC','中国台湾 桃园',24.95,121.20,'pcb','高速覆铜板（AI 服务器基材）。'],
['avc','奇鋐','AVC','中国台湾 新北',25.02,121.45,'power','服务器液冷/散热模组。'],
])
A('SEA',[
['intc-pg','英特尔 槟城/居林','Intel Penang','马来西亚 槟城',5.30,100.27,'pkg','英特尔封测与先进封装基地。'],
['mu-pg','美光 槟城','Micron Penang','马来西亚 槟城 峇六拜',5.29,100.28,'pkg','存储封测工厂。'],
['amd-pg','AMD 槟城','AMD Penang','马来西亚 槟城',5.35,100.29,'pkg','AMD 封测与设计中心。'],
['ifx-kulim','英飞凌 居林','Infineon Kulim','马来西亚 居林',5.43,100.58,'foundry','全球最大 200mm 碳化硅功率晶圆厂（居林高科技园）。'],
['ase-pg','日月光 槟城','ASE Penang','马来西亚 槟城',5.33,100.29,'pkg','封测厂。'],
['ytl-dc','YTL 绿色数据中心园','YTL Green DC Park','马来西亚 柔佛 古来',1.66,103.60,'dc','600MW 园区，部署英伟达 GB200（YTL×NVIDIA）。'],
['jb-dc','柔佛数据中心集群','Johor DC Cluster','马来西亚 柔佛 新山',1.49,103.74,'dc','东南亚增长最快的数据中心集群（Sedenak 等）。'],
['mu-sg','美光 新加坡','Micron Singapore','新加坡 兀兰',1.44,103.79,'mem','NAND 晶圆厂与 HBM 封装新厂。'],
['gf-sg','格芯 新加坡','GlobalFoundries Singapore','新加坡 兀兰',1.45,103.80,'foundry','格芯新加坡晶圆厂。'],
['umc-sg','联电 新加坡','UMC Fab 12i','新加坡 白沙',1.38,103.95,'foundry','12 英寸晶圆厂。'],
['goog-sg','谷歌 新加坡数据中心','Google Singapore DC','新加坡 裕廊西',1.35,103.70,'dc','谷歌云区域数据中心。'],
['fox-vn','富士康 北江/北宁','Foxconn Vietnam','越南 北江',21.27,106.20,'server','电子组装，扩展服务器业务。'],
['ss-bn','三星 北宁','Samsung Bac Ninh','越南 北宁 安丰',21.20,106.00,'device','三星手机工厂。'],
['ss-tn','三星 太原','Samsung Thai Nguyen','越南 太原 安平',21.42,105.86,'device','三星手机工厂。'],
['amkor-vn','安靠 北宁','Amkor Bac Ninh','越南 北宁 安丰2C',21.21,106.02,'pkg','安靠全球最大先进 SiP 封测厂。'],
['intc-vn','英特尔 胡志明','Intel Vietnam','越南 胡志明市',10.85,106.80,'pkg','英特尔最大封测厂（西贡高科技园）。'],
['lux-vn','立讯 越南','Luxshare Vietnam','越南 北江',21.29,106.19,'device','立讯越南组装基地。'],
['zdt-vn','鹏鼎 越南','ZDT Vietnam','越南 北江',21.30,106.22,'pcb','鹏鼎越南 PCB 基地。'],
['victory-vn','胜宏 越南','Victory Giant Vietnam','越南',21.0,106.3,'pcb','2025 年 3 月奠基，在建（具体省份未核实）。'],
['victory-th','胜宏 泰国','Victory Giant Thailand','泰国 大城府',14.35,100.58,'pcb','A1 已量产、A2 2026Q3 量产，AI PCB 基地。'],
['wus-th','沪电 泰国','WUS Thailand','泰国 大城府',14.30,100.62,'pcb','沪电泰国子公司，二期扩建。'],
['kinwong-th','景旺 泰国','Kinwong Thailand','泰国 巴真府',14.05,101.37,'pcb','金池工业园，一期 2026 年初投产。'],
['zdt-th','鹏鼎 泰国','ZDT Thailand','泰国 巴真府',14.03,101.40,'pcb','泰国基地，约 2.5 亿美元投资。'],
['scc-th','深南电路 泰国','Shennan Thailand','泰国 大城府',14.33,100.60,'pcb','泰国新工厂（大城府）。'],
['inno-th','中际旭创 泰国','InnoLight Thailand','泰国 春武里',13.36,101.00,'optic','7 万平方米以上厂房，量产 800G/1.6T。'],
['eopto-th','新易盛 泰国','Eoptolink Thailand','泰国',13.5,100.9,'optic','一期 2023、二期 2025 投产（具体府份未核实）。'],
['tfc-th','天孚通信 泰国','TFC Thailand','泰国 春武里 攀通',13.45,101.09,'optic','光器件与有源产品工厂。'],
['fabrinet','Fabrinet','Fabrinet','泰国 巴吞他尼/春武里',14.08,100.62,'optic','英伟达光模块主要代工方（Pinehurst 与 Chonburi 园区）。'],
['delta-th','台达 泰国','Delta Thailand','泰国 北榄 邦浦',13.52,100.66,'power','服务器/网络电源工厂。'],
['ifx-th','英飞凌 泰国','Infineon Thailand','泰国 北榄',13.60,100.70,'pkg','2025 年动工的后段功率模块工厂。'],
['ti-ph','德州仪器 碧瑶/克拉克','TI Philippines','菲律宾 克拉克',15.18,120.55,'pkg','TI 封测基地（另有碧瑶）。'],
['batam','巴淡岛 数据中心','Nongsa Digital Park','印尼 巴淡岛',1.20,104.10,'dc','服务新加坡的数据中心园区。'],
['mu-in','美光 萨南德','Micron Sanand','印度 古吉拉特 萨南德',22.98,72.38,'pkg','存储封测厂。'],
['tata-fab','塔塔 多雷拉晶圆厂','Tata Dholera Fab','印度 古吉拉特 多雷拉',22.25,72.19,'foundry','印度首座商用晶圆厂（与力积电合作）。'],
['fox-in','富士康 金奈','Foxconn Chennai','印度 金奈 斯里佩鲁姆布杜尔',12.97,79.94,'device','iPhone 组装基地。'],
['delta-in','台达 印度','Delta India','印度 克里希纳吉里',12.52,78.21,'power','电源与基础设施工厂。'],
])
A('JK',[
['ss-pt','三星 平泽','Samsung Pyeongtaek','韩国 平泽',37.02,127.06,'mem','全球最大半导体园区，DRAM/HBM 与代工。'],
['ss-hs','三星 华城/器兴','Samsung Hwaseong','韩国 华城',37.21,127.06,'foundry','三星代工与存储研发。'],
['skh-ic','SK 海力士 利川','SK hynix Icheon','韩国 利川',37.27,127.43,'mem','总部与 HBM 主力产线。'],
['skh-cj','SK 海力士 清州','SK hynix Cheongju','韩国 清州',36.64,127.44,'mem','M15X HBM 新厂。'],
['skh-yi','SK 海力士 龙仁集群','SK hynix Yongin','韩国 龙仁',37.15,127.27,'mem','龙仁半导体集群（在建）。'],
['naver','Naver','Naver','韩国 城南',37.36,127.10,'model','HyperCLOVA X 大模型。'],
['tel','东京电子','Tokyo Electron','日本 东京',35.66,139.74,'equip','涂胶显影/刻蚀/沉积设备。'],
['adv','爱德万测试','Advantest','日本 东京',35.68,139.76,'equip','AI 芯片测试机龙头。'],
['shinetsu','信越化学','Shin-Etsu','日本 东京',35.69,139.77,'mat','全球最大硅片与光刻胶供应商之一。'],
['sumco','胜高','SUMCO','日本 东京',35.67,139.75,'mat','硅片。'],
['jsr','JSR','JSR','日本 东京',35.68,139.75,'mat','光刻胶。'],
['ibiden','揖斐电','Ibiden','日本 岐阜 大垣',35.36,136.61,'pcb','ABF 载板，英伟达主力供应商。'],
['rapidus','Rapidus 北海道','Rapidus','日本 北海道 千岁',42.82,141.65,'foundry','2nm 晶圆厂（IIM-1）。'],
['jasm','台积电 熊本 JASM','TSMC Kumamoto','日本 熊本 菊阳',32.88,130.83,'foundry','台积电日本合资晶圆厂。'],
['disco','迪思科','DISCO','日本 东京',35.66,139.77,'equip','切割与研磨设备（HBM 关键）。'],
['sbg','软银','SoftBank','日本 东京',35.66,139.76,'cloud','Stargate 投资方，持有 Arm。'],
['furukawa','古河电工','Furukawa Electric','日本 东京',35.68,139.76,'optic','光纤与激光器。'],
])
A('EU',[
['asml','阿斯麦','ASML','荷兰 费尔德霍芬',51.41,5.41,'equip','全球唯一 EUV 光刻机供应商。'],
['zeiss','蔡司 SMT','Carl Zeiss SMT','德国 上科亨',48.80,10.10,'equip','EUV 光学系统。'],
['ifx-dd','英飞凌 德累斯顿','Infineon Dresden','德国 德累斯顿',51.12,13.71,'foundry','功率与模拟晶圆厂。'],
['esmc','台积电 ESMC 德累斯顿','ESMC Dresden','德国 德累斯顿',51.13,13.73,'foundry','台积电欧洲合资晶圆厂（在建）。'],
['arm','Arm','Arm','英国 剑桥',52.20,0.13,'eda','CPU IP 架构，英伟达 Grace 等采用。'],
['deepmind','谷歌 DeepMind','Google DeepMind','英国 伦敦',51.53,-0.13,'model','Gemini 模型研发核心。'],
['mistral','Mistral AI','Mistral AI','法国 巴黎',48.87,2.33,'model','欧洲开源大模型代表。'],
['st','意法半导体 克罗尔','STMicro Crolles','法国 克罗尔',45.28,5.88,'foundry','12 英寸晶圆厂。'],
['soitec','Soitec','Soitec','法国 贝尔南',45.22,5.92,'mat','SOI 晶圆（硅光基材）。'],
['nokia','诺基亚','Nokia','芬兰 埃斯波',60.21,24.66,'net','数据中心网络与光传输（收购 Infinera）。'],
['sap','SAP','SAP','德国 瓦尔多夫',49.29,8.64,'ent','企业软件与 Joule AI。'],
['schneider','施耐德电气','Schneider Electric','法国 吕埃尔-马尔迈松',48.88,2.18,'power','数据中心配电与液冷。'],
['asmi','ASM 国际','ASM International','荷兰 阿尔梅勒',52.37,5.22,'equip','ALD 沉积设备。'],
['besi','Besi','Besi','荷兰 杜文',51.95,6.02,'equip','混合键合设备（HBM/先进封装）。'],
])
A('ME',[
['g42','G42 / 星际之门阿联酋','G42 / Stargate UAE','阿联酋 阿布扎比',24.45,54.38,'dc','5GW 阿联酋-美国 AI 园区，首期 1GW Stargate UAE。'],
['humain','HUMAIN','HUMAIN','沙特 利雅得',24.71,46.68,'dc','沙特 PIF 旗下 AI 公司，建设大型数据中心。'],
['nvda-il','英伟达 以色列 (Mellanox)','NVIDIA Israel','以色列 约克尼姆',32.66,35.11,'net','InfiniBand/Spectrum-X 网络研发核心。'],
['intc-il','英特尔 基里亚特盖特','Intel Kiryat Gat','以色列 基里亚特盖特',31.61,34.77,'foundry','英特尔以色列晶圆厂。'],
['tower','高塔半导体','Tower Semiconductor','以色列 米格达勒埃梅克',32.67,35.24,'foundry','硅光/模拟代工。'],
])
SEG={
'design':['芯片设计','up','设计'],'eda':['EDA/IP','up','EDA'],'equip':['半导体设备','up','设备'],'mat':['材料','up','材料'],
'foundry':['晶圆代工','up','代工'],'mem':['存储/HBM','up','存储'],'pkg':['先进封装/封测','up','封测'],'pcb':['PCB/载板','up','PCB'],
'optic':['光模块/光器件','up','光'],'server':['服务器ODM/整机','up','服务器'],'net':['网络设备/连接','up','网络'],'power':['电源/液冷/能源','up','电源'],
'dc':['数据中心/算力园区','mid','IDC'],'cloud':['云/GPU云','mid','云'],'model':['基础模型','mid','模型'],'data':['数据平台','mid','数据'],
'ent':['企业软件','down','软件'],'auto':['自动驾驶/智能车','down','智驾'],'robot':['机器人/具身','down','机器人'],'device':['消费电子/终端','down','终端'],
'med':['医疗','down','医疗'],'ind':['工业','down','工业'],'def':['国防','down','国防']}
REG={'US':'美国','CN':'中国大陆','TW':'中国台湾','SEA':'东南亚/南亚','JK':'日韩','EU':'欧洲','ME':'中东/以色列'}
ids=[s[0] for s in S];assert len(ids)==len(set(ids)),[i for i in ids if ids.count(i)>1]
ARCS=[['asml','tsmc-hc'],['asml','tsmc-tn'],['asml','ss-pt'],['asml','skh-ic'],['zeiss','asml'],['tel','tsmc-tn'],['amat','tsmc-tn'],['lrcx','tsmc-ks'],['shinetsu','tsmc-hc'],['sumco','tsmc-tn'],
['tsmc-tn','nvda'],['tsmc-cowos','nvda'],['tsmc-tn','amd'],['tsmc-tn','aapl'],['tsmc-hc','avgo'],['tsmc-az','nvda'],['skh-ic','nvda'],['skh-cj','nvda'],['ss-pt','amd'],['mu','nvda'],
['ibiden','tsmc-cowos'],['unimicron','tsmc-cowos'],['victory','nvda'],['wus','csco'],['victory-th','nvda'],
['innolight','nvda'],['innolight-sz','goog-ia'],['inno-th','meta-oh'],['eoptolink','aws-va'],['eopto-th','aws-oh'],['tfc','innolight-sz'],['fabrinet','nvda'],['yj','innolight-sz'],['glw','aws-va'],['cohr','msft'],
['nvda','hh'],['nvda','quanta'],['nvda','wistron'],['hh','stargate'],['quanta','meta-ia'],['wiwynn','msft'],['fii','xai'],['delta','stargate'],['nvda','stargate'],['nvda','crwv'],['nvda','xai'],['nvda','g42'],['nvda','ytl-dc'],['nvda','humain'],
['stargate','oai'],['crwv','oai'],['aws-va','anth'],['goog-or','goog'],['msft','oai'],['oai','crm'],['goog','waymo'],['nvda','tsla'],['nvda','figure'],['amkor-vn','nvda'],['intc-pg','intc'],['arm','nvda'],['nvda-il','nvda'],
['smic','hisi'],['smic','camb'],['smic-bj','hygon'],['cxmt','hisi'],['ymtc','inspur'],['naura','smic'],['amec','smic'],['nsig','smic'],['jcet','hisi'],['tfme','amd'],
['hisi','dc-gz'],['hisi','dc-nm'],['inspur','dc-nx'],['inspur','ali'],['sugon','volc'],['camb','volc'],['fii','tc'],['victory','fii'],['scc','hisi'],['accelink','ali'],['eoptolink','volc'],
['dc-wlcb','ali'],['dc-gz','tc'],['dc-nx','ds'],['dc-qy','tc'],['dc-csj','ali'],['ali','unitree'],['bidu','apollo'],['horizon','byd'],['hisi','byd'],['ds','iflytek'],['mthreads','zhipu'],['biren','sense'],['metax','minimax'],['hwc','hisi'],
]
ARCS+=[["jsr-yk", "tsmc-tn"], ["jsr-yk", "ss-pt"], ["tok", "tsmc-hc"], ["tok", "ss-hs"], ["shinetsu-nt", "tsmc-tn"], ["shinetsu-nt", "skh-ic"], ["sumi", "ss-pt"], ["sumi", "tsmc-hc"], ["ffem", "tsmc-hc"], ["ffem", "jasm"], ["tel-ks", "tsmc-tn"], ["tel-ks", "smic"], ["tel-ks", "ymtc"], ["screen", "tsmc-hc"], ["screen", "ss-pt"], ["nikon", "smic"], ["canon", "hua-wx"], ["bjkh", "smic"], ["bjkh", "ymtc"], ["bjkh", "hua"], ["nata", "smic"], ["jingrui", "smic"], ["sinyang", "hua"], ["bokang", "bjkh"], ["hengkun", "ymtc"], ["hengkun", "smic"], ["qiangli", "bjkh"], ["kingsemi", "smic"], ["kingsemi", "ymtc"], ["kingsemi", "hua"], ["uprec", "smee"], ["rdav", "hua-wx"]]
for a,b in ARCS: assert a in ids and b in ids,(a,b)
SRC='数据来源：公司官网/年报/投资者关系记录（巨潮资讯）、Natural Earth、公开新闻报道（如 InvestPenang、Amkor 新闻稿、Infineon 新闻稿、Fabrinet 官网、景旺电子官网、证券日报、高盛调研纪要转述）。坐标为城市/园区级近似。'
out={'segments':SEG,'regions':REG,'sites':S,'arcs':ARCS,'sources':SRC}
open('/workspace/ai-globe/data.js','w').write('// 全球 AI 产业链数据 — '+SRC+'\nwindow.AI_DATA='+json.dumps(out,ensure_ascii=False,indent=0)+';\n')
from collections import Counter
print(len(S),Counter(s[7] for s in S),Counter(SEG[s[6]][1] for s in S))
print(Counter(s[6] for s in S))
