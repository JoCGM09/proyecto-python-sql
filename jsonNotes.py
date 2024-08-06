import json

## un json en python se comporta como un diccionario
people_string = '''
{
    "people": [
        {
            "name":"Jose Carlos",
            "phone":"453434534",
            "emails":["test@gmail.com", "test2@gmail.com"],
            "has_license": false    
        },
        {
            "name": "Juan Carlos",
            "phone": "34534534"
            "emails": null,
            "has_license": true
        }
    ]
}
'''