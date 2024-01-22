def conversion(blocks):
    for block in blocks:
        code = block_data[block["block_id"]]["code"]
        total_code = code.format(block["values"])
        print(total_code)


blocks = [{
        "block_type":"print",
        "block_id":"1",
        "values":"hello world"
    }
]
block_data = {
    "0":{
        "name":"Start block",
        "btype":"starter",
        "color":"yellow",
        "code":""
    },
    "1":{
        "name":"print",
        "btype":"block",
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
            "name":"text",
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
        "code":"",
        "values":{
            "value1":"text"
        }
    }
}
conversion(blocks)