import urllib.parse
import urllib.request
import codecs

uri = 'http://www.xmfg.gov.cn/webinfo/allSaleState.aspx?flag=3'

#the http headers are useful to simulate a particular browser (some sites deny
#access to non-browsers (bots, etc.)
#also needed to pass the content type. 
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,*/*; q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# we group the form fields and their values in a list (any
# iterable, actually) of name-value tuples.  This helps
# with clarity and also makes it easy to later encoding of them.

formFields = (
   ('__VIEWSTATE', r'/wEPDwUKLTI3NTYzNTAwOA9kFgJmD2QWAgIDD2QWAgIBD2QWBAIDDxAPFgYeDURhdGFUZXh0RmllbGQFCHNob3d0ZXh0Hg5EYXRhVmFsdWVGaWVsZAUFdmFsdWUeC18hRGF0YUJvdW5kZ2QQFQoIMjAwNyDlubQIMjAwOCDlubQIMjAwOSDlubQIMjAxMCDlubQIMjAxMSDlubQIMjAxMiDlubQIMjAxMyDlubQIMjAxNCDlubQIMjAxNSDlubQIMjAxNiDlubQVCgQyMDA3BDIwMDgEMjAwOQQyMDEwBDIwMTEEMjAxMgQyMDEzBDIwMTQEMjAxNQQyMDE2FCsDCmdnZ2dnZ2dnZ2dkZAIJDxYCHglpbm5lcmh0bWwFBuWMuuWfn2QYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFJmN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkSW1hZ2VCdXR0b24yRea9SzpKoN1sKkjoLdhxjomNyvS3WthxMk7gCk0yaNw='),
    ('__VIEWSTATEGENERATOR','3A341B33'),
   ('__EVENTVALIDATION', '/wEdAB2SBLRoTEwZoOybVm2Cu1JBvpdIzOqLdm+HDUQxavy+7EiauNjHK/R3qqf6LVt4s7pEu9GkptM7L6W3VWk/iuQn+dVxE3H2l7dP2cCCSH2QK4UMIlLE+plOlxvV/P0VS2PQD6Xvn4WeQoURxS/XRa1IFgKcpwTDkC+9+885LEHhaGa3Nrcuptv8vXb5l7Jgy/T1/9OrEKjxwQDimb9Vzm1damif7QhradLibgegACxu2Xt3dhhMIGfxfCriTfr1bD1wS5Lpb0T5gNq+yTekurxBGuCYE1nYEuy6oUn1pU00e9UOxW+07wFFxO7uyIyJPeeU6TJZ+gvSShisMf0qsCy9xFPnnnNuEvnV6rCB7QhVlov8gqrgD0NjIraZRPscX5lLpU5V0i4KU/aD+utaRqsn9zBaigMla7ReIkQr+ieUHLKMW3qHuu33Mw8/oa4i2Fp6Qmon5LbM9BW53JX8xF/p2fGiLETihxLBOFdgZqhmBqTjD6OHlKeOmOF/JQPJXa+sSwftJIgYW6xlYeONYYGkpDb8uXN7+8QWsEa7QRAy4cxqyigIsRlDOmD9lyf9OhS4PCntqx+RiozjAHGKc3mnH6UXTw3Sf0i4qbJFleIfLHNXXtjhnYMzMIKftIAMMfk4gA8fJwItUjLBHIa8l0lv'),
   ('ctl00$ContentPlaceHolder1$DropDownList1', '2016'),
   ('ctl00$ContentPlaceHolder1$DropDownList2', '7'),
   ('ctl00$ContentPlaceHolder1$ImageButton2', '19'),
   ('ctl00$ContentPlaceHolder1$ImageButton2', '6'),
   ('ctl00$ContentPlaceHolder1$flaghidden', '1'),
   ('ctl00$ContentPlaceHolder1$yearhidden', ''),
   ('ctl00$ContentPlaceHolder1$monthhidden', ''),
   ('ctl00$ContentPlaceHolder1$constrhidden', ''),
)

# these have to be encoded    
encodedFields = urllib.parse.urlencode(formFields)
encodedFields = encodedFields.encode('ascii')
req = urllib.request.Request(uri, encodedFields, headers)
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
f = codecs.open("..\\output\\test.htm","w", "utf-8");
f.write(data);
