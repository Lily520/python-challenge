#13

import xmlrpc.client

if __name__ == "__main__":

    php_html = "http://www.pythonchallenge.com//pc//phonebook.php"
    re_ans1 = xmlrpc.client.ServerProxy(php_html)

    #['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
    print(re_ans1.system.listMethods())
    print(re_ans1.system.methodHelp("phone")) #Returns the phone of a person
    print(re_ans1.system.methodSignature("phone")) #[['string', 'string']]

    result = re_ans1.phone("Bert") #555-ITALY
    print(result)