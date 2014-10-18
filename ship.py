from xml.dom.minidom import Document
doc = Document()

# this should not be in the closing tag
reqshipmentval = doc.createElement('req:ShipmentValidateRequestAP xmlns:req="http://www.dhl.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.dhl.com ship-val-req_AP.xsd"')
doc.appendChild(reqshipmentval)

request = doc.createElement("Request")
reqshipmentval.appendChild(request)


serviceheader = doc.createElement("ServiceHeader")
request.appendChild(serviceheader)


messagetime = doc.createElement("MessageTime")
serviceheader.appendChild(messagetime)
text = doc.createTextNode("Example Message time")
messagetime.appendChild(text)


messagereference = doc.createElement("MessageReference")
serviceheader.appendChild(messagereference)
text = doc.createTextNode("Example Message Reference")
# i can use raw_input to caputre the required reference, perhaps password?
# text = doc.createTextNode(raw_input("What do you want your reference to be? "))
messagereference.appendChild(text)


siteid = doc.createElement("SiteID")
serviceheader.appendChild(siteid)
text = doc.createTextNode("User ID")
siteid.appendChild(text)


pword = doc.createElement("Password")
serviceheader.appendChild(pword)
text = doc.createTextNode("PA44word")
pword.appendChild(text)



filename = "ship.xml"
f = open(filename, "w")
f.write(doc.toprettyxml (indent = "	"))
f.close()
