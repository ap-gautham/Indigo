def hello():
    print('Hi')
    print('Test')

def query_vizier_catalog(catalogue = "J/MNRAS/508/3877", query_table_name = 'maincat', query_object_count = 10, query_cols = '*', cross_match_col = None, cross_match_objects = None):
    
    catalogue_ivoid = f"ivo://CDS.VizieR/{catalogue}"
    voresource = registry.search(ivoid=catalogue_ivoid)[0]
    
    tables = voresource.get_tables()
    tables_names = np.array(list(tables.keys()))
    
    query_table = tables_names[[(catalogue + '/' + query_table_name) == i for i in tables_names]][0]

    if cross_match_objects is not None:
        query_object_count = len(cross_match_objects)
    
    if cross_match_col is not None:
        tap_records = voresource.get_service("tap").run_sync(
        f'SELECT TOP %d'%(query_object_count) + " " + query_cols + f' FROM "{query_table}"\
        WHERE "{cross_match_col}" IN ' + str(tuple(cross_match_objects)),
        )
    else :
        tap_records = voresource.get_service("tap").run_sync(
        f'SELECT TOP %d'%(query_object_count) + " " + query_cols + f' FROM "{query_table}"',
        )
    
    tap_table = tap_records.to_table()
    return tap_table