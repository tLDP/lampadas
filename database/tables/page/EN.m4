m4_dnl name                  template    menu    order   data                dyn reg adm sysadmin
insert(index,                splash,     [],         0,  [],                 f,  f,  f,  f)
                             
insert(home,                 index,      main,       1,  [],                 f,  f,  f,  f)
insert(my,                   default,    main,       2,  [],                 t,  t,  f,  f)
insert(doctable,             default,    main,       3,  [],                 f,  f,  f,  f)
insert(search,               default,    main,       4,  [],                 t,  f,  f,  f)
                                                                                 
insert(sessions,             default,    admin,      1,  [],                 t,  f,  f,  t)
insert(users,                default,    admin,      2,  [letter],           t,  f,  t,  f)
insert(adduser,              default,    admin,      3,  [],                 t,  f,  t,  f)
insert(errors,               default,    admin,      4,  [],                 t,  f,  t,  f)
insert(adddocument,          default,    admin,      5,  [],                 t,  t,  t,  f)
insert(news,                 default,    admin,      6,  [],                 f,  f,  t,  f)
insert(addnews,              default,    admin,      7,  [],                 f,  f,  t,  f)
insert(pages,                default,    admin,      8,  [],                 f,  f,  t,  f)                             
insert(addpage,              default,    admin,      9,  [],                 f,  f,  t,  f)
insert(strings,              default,    admin,     10,  [],                 f,  f,  t,  f)                             
insert(addstring,            default,    admin,     11,  [],                 f,  f,  t,  f)

insert(recentnews,           default,    news,       1,  [],                 f,  f,  f,  f)
insert(stats,                default,    news,       2,  [],                 f,  f,  f,  f)
                                                                                 
insert(staff,                default,    volunteer,  1,  [],                 f,  f,  f,  f)
insert(contribute,           default,    volunteer,  2,  [],                 f,  f,  f,  f)
insert(unmaintained,         default,    volunteer,  3,  [],                 f,  f,  f,  f)
insert(maint_wanted,         default,    volunteer,  4,  [],                 f,  f,  f,  f)
insert(pending,              default,    volunteer,  5,  [],                 f,  f,  f,  f)
insert(wishlist,             default,    volunteer,  6,  [],                 f,  f,  f,  f)
insert(resources,            default,    volunteer,  7,  [],                 f,  f,  f,  f)
insert(maillists,            default,    volunteer,  8,  [],                 f,  f,  f,  f)
                                                                                 
insert(about,                default,    help,       1,  [],                 f,  f,  f,  f)
insert(lampadas,             default,    help,       2,  [],                 f,  f,  f,  f)
insert(copyright,            default,    help,       3,  [],                 f,  f,  f,  f)
insert(privacy,              default,    help,       4,  [],                 f,  f,  f,  f)
insert(sitemap,              default,    help,       5,  [],                 f,  f,  f,  f)
                                                                                 
insert(newuser,              default,    [],         0,  [],                 t,  f,  f,  f)
insert(mailpass,             default,    [],         0,  [],                 t,  f,  f,  f)
insert(topic,                default,    [],         0,  [topic],            t,  f,  f,  f)
insert(document,             default,    [],         0,  [doc],              t,  t,  f,  f)
insert(document_main,        default,    [],         0,  [doc],              t,  t,  f,  f)
insert(document_files,       default,    [],         0,  [doc],              t,  t,  f,  f)
insert(document_users,       default,    [],         0,  [doc],              t,  t,  f,  f)
insert(document_revs,        default,    [],         0,  [doc],              t,  t,  f,  f)
insert(document_topics,      default,    [],         0,  [doc],              t,  t,  f,  f)
insert(document_notes,       default,    [],         0,  [doc],              t,  t,  f,  f)
insert(document_translation, default,    [],         0,  [doc],              t,  t,  f,  f)
insert(document_admin,       default,    [],         0,  [doc],              t,  t,  f,  f)
insert(news_edit,            default,    [],         0,  [news],             f,  f,  t,  f)
insert(page_edit,            default,    [],         0,  [page],             f,  f,  t,  f)
insert(string_edit,          default,    [],         0,  [string],           f,  f,  t,  f)
insert(404,                  default,    [],         0,  [],                 t,  f,  f,  f)
insert(user_exists,          default,    [],         0,  [],                 t,  f,  f,  f)
insert(username_required,    default,    [],         0,  [],                 t,  f,  f,  f)
insert(email_exists,         default,    [],         0,  [],                 t,  f,  f,  f)
insert(account_created,      default,    [],         0,  [],                 t,  f,  f,  f)
insert(password_mailed,      default,    [],         0,  [],                 t,  f,  f,  f)
insert(user,                 default,    [],         0,  [user],             t,  f,  f,  f)
insert(logged_in,            default,    [],         0,  [],                 t,  f,  f,  f)
insert(logged_out,           default,    [],         0,  [],                 t,  f,  f,  f)
insert(type,                 default,    [],         0,  [type],             t,  f,  f,  f)
insert(sourcefile,           default,    [],         0,  [filename],         t,  t,  f,  f)
insert(file_report,          default,    [],         0,  [report filename],  t,  t,  f,  f)
insert(collection,           default,    [],         0,  [collection],       f,  f,  f,  f)
