'''Assignment 5: Deep JSON/Configuration Key Traverser
Scenario
Configuration files loaded from JSON databases consist of nested dictionary hierarchies. 
Checking key existence at every level using nested conditions (if key in dictionary) leads 
to complex and verbose code. You need to write a clean traverser utility that navigates nested 
dictionaries using exceptions.'''

def traverse_nested_config(config_dict, path_str, default=None):
    path=path_str.split('.')
    try:
        return config_dict[path[0]][path[1]][path[2]]
    except KeyError:
        return default
    except TypeError:
        return default
            
def main():
    config = {"server": 
              {"host": "127.0.0.1",
               "port": 8080,
                "ssl": {"enabled": True,
                        "cert_path": "/etc/ssl/certs"}},
                         "database": "postgresql://localhost:5432"}
    print(traverse_nested_config(config, "server.ssl.cert_path"))
    print(traverse_nested_config(config, "server.ssl.host","Guest"))
    print(traverse_nested_config(config,"database.host","localhost"))
main()