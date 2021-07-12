import pytesseract
from PIL import Image
#把现在的图片读取出来

# image = Image.open("E:/capacha2.png")
# text = pytesseract.image_to_string(image)
from util.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/932-2","152112","eb751725cacf4e3b9adba25454f13557" )
r.addBodyPara("length", "4")
r.addBodyPara("specials", "false")
r.addBodyPara("secure", "true")

r.addFilePara("image",r"E:/capacha2.png")
res = r.post()
# text = res.json()["showapi_res_body"]['result']
print(res.text) # 返回信息
