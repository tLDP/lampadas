insert([blkhead],
[
    <head>
        <title>|title|</title>
        <link rel="stylesheet" href="|uri.base|css/ldp.css" type="text/css">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
])

insert([blklogo],
[
    <table class="logo">
      <tr>
        <td valign="middle">
          LOGO
        </td>
      </tr>
    </table>
])

insert([blkheader],
[
    <table class="header" width="100%">
      <tr>
        <td>
          <h1>|strproject|</h1>
          <h2>|title|</h2>
        </td>
      </tr>
    </table>
])

insert([blkfooter],
[
    <table class="footer" width="100%">
      <tr>
        <td>
          <a href="|uri.base|copyright|uri.lang_ext|">|strcopyright|</a> \\|
          <a href="|uri.base|privacy|uri.lang_ext|">|strprivacy|</a> \\|
          <a href="|uri.base|lampadas|uri.lang_ext|">|strabout_lamp|</a>
        </td>
      </tr>
    </table>
    <center>
      <a href="http://www.python.org"><img src="|uri.base|images/PythonPowered.gif" alt="Python Powered!"></a>
      <a href="http://www.opensource.org"><img src="http://www.opensource.org/trademarks/osi-certified/web/osi-certified-90x75.png" height=75 width=90 alt="OSI Certified"></a>
      <a href="http://www.gnome.org"><img src="|uri.base|images/gnome2.png" height="48" width="48" alt="Gnome"></a>
      <a href="http://www.tldp.org"><img src="|uri.base|images/ldp.gif" height="60" width="150" alt="TLDP"></a>
      <br>|strrender_time|: |elapsed_time|
    </center>
])

insert([blknopermission],
[
    <table class="box" width="100%">
      <tr>
        <th>|strerror|</th>
      </tr>
      <tr>
        <td>|strnopermission|</td>
      </tr>
    </table>
])

insert([blknotfound],
[
    <table class="box" width="100%">
      <tr>
        <th>|strerror|</th>
      </tr>
      <tr>
        <td>|strnotfound|</td>
      </tr>
    </table>
])

insert([blkdocument_tabs],
[
    <table class="tab">
        <tr>
            <td><a href="|uri.base|document_main/|uri.id||uri.lang_ext|">|strdetails|</a></td>
            <td><a href="|uri.base|document_files/|uri.id||uri.lang_ext|">|strfiles|</a></td>
            <td><a href="|uri.base|document_revs/|uri.id||uri.lang_ext|">|strversions|</a></td>
            <td><a href="|uri.base|document_topics/|uri.id||uri.lang_ext|">|strtopics|</a></td>
            <td><a href="|uri.base|document_users/|uri.id||uri.lang_ext|">|strusers|</a></td>
            <td><a href="|uri.base|document_notes/|uri.id||uri.lang_ext|">|strnotes|</a></td>
            <td><a href="|uri.base|document/|uri.id||uri.lang_ext|">|strall|</a></td>
        </tr>
    </table>
])
