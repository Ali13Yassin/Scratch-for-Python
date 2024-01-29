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
        "code":"#Code starts here"
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
            "value1":"custom"
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
    }, 
    "2":{ #String
        "code":'"{}"'
    },
    "3":{ #Int
        "code":"int({})"
    },
    "4":{ #Float
        "code":"float({})"
    },
    "custom":{ #Custom code
        "code":"{}"
    }
}

def compileblocks(blocks):
    lines = ""
    for block in blocks:
        var = [] #This will store all the values to format into the code
        code = all_blocks[block["block_id"]]["code"] #Get the code
        for key in block["values"]:
            if block["values"][key][1].isdigit(): #If value type is a number
                varcode = var_types[block["values"][key][1]]["code"] #Get the code for the value type
                var.append(varcode.format(block["values"][key][0])) #Add the value to the var list
            else:
                var.append(smol_compile(key, block["values"][key])) #Add the value to the var list
        line = code.format(*var) #Format the code with the values
        lines = lines + line + "\n" #Add the line to the total code
    return lines #Return the total code

#This will compile the values inside the small blocks and return code
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
        "block_id":"0",
        "values":{
            "value1":["This is a test","0"]
                  }
    },
    {
        "block_type":"1",#Normal
        "block_id":"2",
        "values":{
            "value1":["That the compiler works","2"],
            "value2":["test","2"]
                  }
    }
]
print(compileblocks(blocks))