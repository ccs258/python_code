# -*- coding: utf-8 -*-
# @Time    : 19-2-13 下午9:39
# @Author  : ccs
import pandas as pd
df = pd.read_csv('C:/Users/ccs/Desktop/xzqh.csv',sep=',',encoding='gbk') ##表明需要是英文名？
print(df[1:10])

code_mapping = {}
for index,row in df.iterrows():
    if row['yb']:
        code_mapping[str(row['yb'])] = row['qh']
    else:
        continue

print(code_mapping)


"""
#电子牌发牌详情
{'电子牌序号': 'id1', '发卡原因（代码）': 'id2', '发卡时间': 'id3', '发卡单位代码': 'id4', '发卡单位名称': 'id5', '发卡人ID': 'id6', '发卡人姓名': 'id7', '发卡点编号': 'id8', '发卡点名称': 'id9', '卡状态        ': 'id10', '注销原因': 'id11', '注销原因说明': 'id12', '注销时间': 'id13', '注销单位代码': 'id14', '注销单位名称': 'id15', '注销人ID': 'id16', '注销人姓名': 'id17', '机动车序号': 'id18', '号牌省份': 'id19', '号牌种类': 'id20', '号牌号码': 'id21', '车辆识别代号': 'id22', '车辆类型': 'id23', '使用性质': 'id24', '审验截止日期': 'id25', '写卡时间': 'id26', '写卡单位代码': 'id27', '写卡单位名称': 'id28', '写卡操作人': 'id29', '写卡操作人名称  ': 'id30', ' 写卡原因': 'id31', '写卡点编号': 'id32', '写卡点名称': 'id33', '写卡读写器设备电路版号': 'id34', '转递记录类型': 'id35', '主城区车辆': 'id36', '发卡原因（中文）': 'id37', '车辆领卡顺序号': 'id38'}

#电子牌记录
{'采集ID号': 'from_id', 'EPC码': 'epc', '电子牌卡号': 'EID', '车牌号': 'content1', '档案号': 'content2', '采集点名称': 'reader', '采集天线号': 'antenna', '采集时间': 'time', '采集状态': 'result', 'USER区': 'user126', '阅读器IP': 'readerIP', '数据条数': 'id', '来源服务器IP': 'fromserverip', '写入时间': 'inserttime'}

#驾驶人详情
{'档案编号': 'DABH', '准驾车型': 'ZJCX', '初次领证日期': 'CCLZRQ', '有效期始': 'YXQS', '有效期止': 'YXQZ', '累计计分': 'LJJF', '管理编码': 'GLBM', '身份证明编码': 'SFZMHM', '身份证明名称': 'SFZMMC', '姓名': 'XM', '性别': 'XB', '出生日期': 'CSRQ', '国籍': 'GJ', '行政区号': 'DJZSXZQH', '地址': 'DJZSXXDZ', '邮编': 'DJZSYZBM', '联系住所行政区号': 'LXZSXZQH', '联系住所信息地址': 'LXZSXXDZ', '联系住所邮政编号': 'LXZSYZBM', '联系电话': 'LXDH'}


#机动车数据表
{'车辆档案号': 'XH', '车辆识别代号': 'CLSBDH', '发动机号': 'FDJH', '号牌种类（代码）': 'HPZL', '号牌种类名称': 'hpzl_name', '车牌号': 'hphm_no', '制造厂名称': 'ZZCMC', '车辆品牌': 'CLPP1', '车辆型号': 'CLXH', '车辆类型（代码）': 'CLLX', '车辆类型名称': 'cllx_name', '使用性质（代码）': 'SYXZ', '使用性质名称': 'syxz_name', '获得方式（代码）': 'HDFS', '获得方式名称': 'hdfs_name', '车身颜色（代码）': 'CSYS', '车身颜色名称': 'csys_name', '出厂日期': 'CCRQ', '所有人': 'SYR', '联系电话': 'LXDH', '详细地址': 'ZSXXDZ', '行政区划': 'ZSXZQH', '邮政编码': 'YZBM1', nan: 'ys', '初次登记日期': 'CCDJRQ', '核定载质量': 'HDZZL', '核定载客': 'HDZK', '发动机型号': 'FDJXH', '燃料种类名称': 'rlzl_name', '燃料种类（代码）': 'RLZL', '总质量': 'ZZL', '整备质量': 'ZBZL', '前排载客': 'QPZK', '后排载客': 'HPZK', '定检日期': 'DJRQ', '制造国名称': 'zzg_name', '制造国（代码）': 'ZZG', '有效期止': 'YXQZ', '发证日期': 'FZRQ', '车外扩长': 'CWKC', '轮胎规格': 'LTGG', '轴数': 'ZS', '轮胎数': 'lts', '准牵引质量': 'ZQYZL', '排量': 'PL'}

#RFID设备表
{'采集点编号': 'cjdid', '采集点方向': 'fx', '设备IP': 'equipment_rfid'}

#zp设备表
{'采集点编号': 'cjdid', '采集点方向': 'fx', '设备IP': 'equipment_ip'}

#采集方向与经纬度表
{'采集点编号': 'cjdid', '方向1': 'fx1', '方向2': 'fx2', '方向3': 'fx3', '杆架类型': 'gjlx', '记录时间': 'inserttime', '经纬度_经度': 's_jwd_jd', '经纬度_纬度': 's_jwd_wd', nan: nan}

#RFID设备采集数据
{'采集ID号': 'id', 'EPC码（车型和车辆使用性质）': 'EPC', '电子牌卡号': 'EID', '车牌号': 'CONTENT1', '档案号': 'CONTENT2', '采集点名称': 'READER', '采集天线号': 'ANTENNA', '采集时间': 'TIME', '采集状态': 'RESULT', '阅读器IP': 'READERIP', nan: nan}

#抓拍1数据
{'记录ID号': 'RECORD_ID', '卡口编号': 'TOLLGATE_CODE2', '车道编号': 'LANE_INDEX2', '车道类型': 'LANE_DIR2', '经过时刻': 'PASS_TIME2', '号牌数量': 'PLATE_NUMBER', '号牌一致': 'PLATE_COINCIDE', '号牌颜色': 'PLATE_COLOR', '号牌种类': 'PLATE_TYPE', '尾部号牌置信度(即是车牌号码)': 'BACKEND_PLATE_CODE', '尾部号牌颜色': 'BACKEND_PLATE_COLOR', '尾部号牌种类': 'BACKEND_PLATE_TYPE', '车辆品牌': 'VEHICLE_BRAND', '车身颜色深浅': 'VEHICLE_COLORDEPTH', '车身颜色': 'VEHICLE_COLOR', '车辆类型': 'VEHICLE_TYPE', '车外廓长': 'VEHICLE_LENGTH', '车辆速度': 'VEHICLE_SPEED', '执法限速': 'LIMIT_SPEED', '行驶状态': 'DRIVE_STATUS', '图像数量': 'PIC_NUMBER', '第1张图像路径': 'PIC1_NAME', '第2张图像路径': 'PIC2_NAME', '第3张图像路径': 'PIC3_NAME', '第4张图像路径': 'PIC4_NAME', '车牌图像路径': 'PLATE_PIC', '识别时间': 'IDENTIFY_TIME', '识别状态': 'IDENTIFY_STATUS', '处理标记': 'DEAL_TAG', nan: 'BUTTED_TRANS_FLAG2', '地点编号': 'PLACE_CODE', '采集类型': 'EQUIPMENT_TYPE', '更新时间': 'UPDATE_TIME', '号牌置信度': 'PLATE_CONFIDENCE', '尾部号牌置信度': 'REAR_PLATE_CONFIDENCE'}


#抓拍2数据
{'记录ID号': 'RECORD_ID', '卡口编号': 'TOLLGATE_CODE', '车道编号': 'LANE_INDEX', '车道类型': 'LANE_DIR', '经过时刻': 'PASS_TIME2', '号牌数量': 'PLATE_NUMBER', '号牌一致': 'PLATE_COINCIDE', '号牌颜色': 'PLATE_COLOR', '号牌种类': 'PLATE_TYPE', '尾部号牌置信度(即是车牌号码)': 'BACKEND_PLATE_CODE', '尾部号牌颜色': 'BACKEND_PLATE_COLOR', '尾部号牌种类': 'BACKEND_PLATE_TYPE', '车辆品牌': 'VEHICLE_BRAND', '车身颜色深浅': 'VEHICLE_COLORDEPTH', '车身颜色': 'VEHICLE_COLOR', '车辆类型': 'VEHICLE_TYPE', '车外廓长': 'VEHICLE_LENGTH', '车辆速度': 'VEHICLE_SPEED', '执法限速': 'LIMIT_SPEED', '行驶状态': 'DRIVE_STATUS', '图像数量': 'PIC_NUMBER', '第1张图像路径': 'PIC1_NAME', '第2张图像路径': 'PIC2_NAME', '第3张图像路径': 'PIC3_NAME', '第4张图像路径': 'PIC4_NAME', '车牌照片路径': 'PLATE_PIC', '识别时间': 'IDENTIFY_TIME', '识别状态': 'IDENTIFY_STATUS', '处理标记': 'DEAL_TAG', '地点编号': 'PLACE_CODE', '采集类型': 'EQUIPMENT_TYPE', '更新时间': 'UPDATE_TIME', '号牌置信度': 'PLATE_CONFIDENCE', '尾部号牌置信度': 'REAR_PLATE_CONFIDENCE'}

#保险数据详细版本
{'ID': '主键', 'REPORT_CODE': '报案编号', 'AUDIT_CODE': '审批编号', 'REPORT_NO': '报告编号', 'INSURANCE_COMP_ID': '保险公司', 'APPLY_TYPE': '查询类型', 'DRIVER': '驾驶人', 'ID_NUMBER': '身份证号', 'DRIVER_LICENCE_ID': '驾驶证号', 'PLATE': '车牌', 'PLATE_COLOR': '车牌颜色', 'VEHICLE_MODEL': '车辆品牌', 'OCCUR_TIME': '出险时间', 'PROPOSER': '申请人', 'APPLY_TIME': '申请时间', 'AUDITOR': '好运通坐席', 'ASSESSMENT_OF_LOSS': '估损金额', 'ATTACHMENT': '附件', 'SEARCH_REASON': '查询原因', 'SEARCH_START': '查询申请时间', 'SEARCH_END': '查询结束时间', 'ACCIDENT_SPOT': '事故地点', 'STATUS': '状态', 'THIRDPLATE': '三者车牌', 'THIRD_PLATE_COLOR': '三者车牌颜色', 'THIRD_VEHICLE_MODEL': '三者车型', 'THIRD_ASSESSMENT_OF_LOSS': '三者车估价', 'REMARK': '备注', 'DRIVERPHOTO': '驾驶员照片', 'ACCIDENTPHOTO': '事故照片路径', 'ISTHIRDJOIN': '是否第三方公司参与', 'ACCIDENTTYPE': '事故类型', 'QUERY_RESULTS': '查询结果', 'COMMITMENTID': '承诺函', nan: nan}

"""