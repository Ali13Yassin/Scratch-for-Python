# This file is used to convert the block data into code. 

def conversion(blocks):
    for block in blocks:
        code = block_data[block["block_id"]]["code"]
        for value in block["values"]:
            total_code = code.format(value) #Needs to work for when there are multiple required values
        print(total_code)


blocks = [{
        "block_type":"print",
        "block_id":"1",
        "values":"hello world"
    },
    {
        "block_type":"print",
        "block_id":"Template",
        "values":"hello world"
    },
    {
        "block_type":"",
        "block_id":"",
        "values":{

        }
    }
]
#Types of Blocks:
#Starters = 0
#Normal = 1
#Control blocks = 2
#circle values = 3
#Angular conditions = 4
block_data = {
    "0":{
        "name":"Start block",
        "btype":"0",
        "color":"yellow",
        "code":""
    },
    "1":{
        "name":"print",
        "btype":"1",
        "color":"blue",
        "code":"print({})",
        "num_values":1
    },
    "2":{
        "name":"Set Variable {} as {}",
        "btype":"block",
        "color":"orange",
        "code":"{} = {}",
        "values":{
            "name":"str",
            "value":"any"
        }
    },
    "custom":{
        "name":"Custom code",
        "btype":"block",
        "color":"purple",
        "code":"",
        "values":{
            "value1":"text"
        }
    },
    "Template":{
        "name":"",
        "btype":"",
        "color":"",
        "code":"code{}",
        "values":{
            "value1":"text"
        }
    }
}
block_types = {
    "0":{
        "block_img":"img",
        "snap":"bottom",
    }
}

var_types = {
    "0":{ #Input
        "code":"input({})"
    },
    "1": { #Bolean
        "code":"{}"
    }, #String
    "2":{
        "code":'"{}"'
    },
    "3":{ #Int
        "code":"{}"
    },
    "4":{ #Float
        "code":"{}"
    }
}
conversion(blocks)