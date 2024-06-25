template_prompts = ['''
我们的雷达产品以太网配置如下， 
协议版本: 2011 domain number: 0 BMCA设置: 关闭 
Announce Message: Disabled Signaling Message: Enabled by default
asCapable: TRUE 
Clock type: Hardware Sync interval: 125ms 
Destination MAC Address: 01:80:C2:00:00:0E Ethertype: 0x88F7 
Two Step mode only 
支持预定义Path Delay和Freq Ration 角色：slave PDelay Interval: 1秒'''
,
'''我们的嵌入式产品新增工作电压范围9V-16V，
支持5%工作电压波动以及2KV 耐ESD干扰，
通过汽车模拟电源以及ESD干扰设备模拟干扰。'''
,
'''我们的雷达产品以太网配置如下，
运行canoe工程文件，运行capl脚本，
查看trace报文进行测试 
协议版本: 2011
domain number: 0
BMCA设置: 关闭
Announce Message: Disabled
Signaling Message: Enabled by default
asCapable: TRUE 
Clock type: Hardware Sync 
interval: 125ms 
Destination MAC Address: 01:80:C2:00:00:0E 
Ethertype: 0x88F7 Two Step mode only 
支持预定义Path Delay和Freq Ration 角色：slave PDelay 
Interval: 1秒 '''
,
'''我们的雷达产品以太网配置如下，
采用UDP数据传输，
消息ID 0x11E 
payload长度8bytes 以20ms周期性发送,
消息包含起始位0的8bit CRC校验，取值范围0-255;
起始位8的4bit 消息计数，取值范围0-14;
起始位29的1bit 车速校验及初始状态，取值范围0-1;
起始位32的13bit 车速信息，取值范围0-360（无效值1901-1FFF）''']

