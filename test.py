
import json
dic={"k1":"v1"}
# return HttpResponse("func('yuan')")
# return "func('%s')" %json.dumps(dic)


dic2 = "func('%s')" %json.dumps(dic)


print(dic2)