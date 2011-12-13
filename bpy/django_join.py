def main():
    
    q = DjangoModel1.objects.filter(abitfield=1)
    connection = ("`%s`" %DjangoModel1.db_table, "`%s`" %DjangoModel2.db_table, "model2_id", "id")
    q.query.join(connection, always_create=True,promote=True,nullable=True)
    q = q.extra(select={'fkey_id' : "`%s`.`%s`" % (DjangoModul2.db_table,'fkey_id')})
    q8 = dict(q.filter(adate__year=2008).values_list('fkey_id','id'))
    q9 = dict(q.filter(adate__year=2009).values_list('fkey_id','id'))
    q10 = dict(q.filter(adate__year=2010).values_list('fkey_id','id'))
    
    all_stuff={}
    for id in q9.keys():
        try:
            all_stuff[id]=[q9[id],q10[id],q8[id]]
        except:
            pass

    print "I'm here", len(all_stuff.keys())
    
main()
