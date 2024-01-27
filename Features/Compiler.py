#Version 0.1 (Pre-Alpha)
#This code transfers the block data into code through these steps
#1.Use id to get the "code"
#2.Get how many values are in block
#3.Take input values
#4.Transfer all info to code
#5.Restart proccess for next line

#Define all blocks
all_blocks = {
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
        "num_values":1,
        "values":{
            "value1":"text"
        }
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
        "code":"int({})"
    },
    "4":{ #Float
        "code":"{}"
    }
}

def compileblocks(blocks):
    lines = ""
    for block in blocks:
        var = []
        code = all_blocks[block["block_id"]]["code"]
        for key in block["values"]:
            if block["values"][key][1].isdigit():
                varcode = var_types[block["values"][key][1]]["code"]
                var.append(varcode.format(block["values"][key][0]))
            else:
                var.append(smol_compile(key, block["values"][key]))
        line = code.format(*var)
        lines = lines + line + "\n"
        # lines.append(line)
        # lines.append("\n")
    return lines
            
def smol_compile(key, value):
    # if int(all_blocks[block["block_id"]]["btype"]) > 2:
    print("does nothing yet")

blocks = [
    {
        "block_type":"1",#Normal
        "block_id":"1",
        "values":{
            "value1":["hello world","2"]
                  }
    },
    {
        "block_type":"1",#Normal
        "block_id":"1",
        "values":{
            "value1":["This is a test","0"]
                  }
    },
    {
        "block_type":"1",#Normal
        "block_id":"1",
        "values":{
            "value1":["That the compiler works","3"]
                  }
    }
]
print(compileblocks(blocks))