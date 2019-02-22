"""Dojo Model

Usage:
 andela.py create_office <room_names>
 andela.py create_livingspace <room_names>
 andela.py add_fellow <name>
 andela.py add_staff <name>
 andela.py print_office <room>
 andela.py print_livingspace <room>
 py andela.py -h | --help
Examples:
  python andela.py create_office Nairobi
  python andela.py create_livingspace kigali
  python andela.py add_fellow musa
  python andela.py add_staff kim
  python andela.py print_office blue
  python andela.py print_livingspace red


Options:
    -h, --help  Show this screen and exit.
    
"""

import methods

from docopt import docopt



if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments['create_office']:
        office = arguments['<room_names>']
        methods.create_office(office)

    elif arguments['create_livingspace']:
        livingspace =  arguments['<room_names>']
        methods.livingspace(livingspace)

    elif arguments['add_fellow']:
        fellow = arguments['<name>']
        methods.add_felllow(fellow)

    elif arguments['add_staff']:
        staff = arguments['<name>']
        methods.add_staff(staff)

    elif arguments['print_office']:
       room = arguments['<room>']
       methods.print_office(room)

    elif arguments['print_livingspace']:
       room = arguments['<room>']
       methods.living(room)  
    
   
       
     
         
      
      
   
    
