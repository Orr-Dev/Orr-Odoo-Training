{
    'name':'ORR Material Purchase Requsitions Extention',
    'summary': 'This module extends the Material Purchase Requestion',
    'author': 'ORR Dev',
    'depends': [
        'base',
        'purchase',
        'project',
        'material_purchase_requisitions',
    ],
    'application':False,
    'installable':True,
    'data': [
       'views/purchase_requsition_tree_view.xml'
    ]   
}