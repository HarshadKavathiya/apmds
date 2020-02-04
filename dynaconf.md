# Dynaconf Guide for Developer

## Access setting variable in code
    from dynaconf import settings
    
    print(settings.VARIABLE_IN_CONFIG_FILE)
    print(settings.DEBUG)
    
    
## Working environments

    export ENV_FOR_DYNACONF=staging
or 

    ENV_FOR_DYNACONF=staging python yourapp.py