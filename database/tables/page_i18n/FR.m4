insert([newdocument], [Add Document], [],
[
    |tabeditdoc|
])

insert([admin], [Admin Page], [],
[
    <p>Admin tools.
])

insert([users], [User List], [],
[
    |tabusers|
])

insert([sysadmin], [Sysadmin Page], [],
[
    <p>Sysadmin tools.
])

insert([my], [My Home], [],
[
    <p>This is your personal home page.

    <p>This table lists documents you have volunteered to contribute to:

    |session_user_docs|
])

insert([home], [|strproject|], [Home],
[
	<p>Ce syst&egrave;me est en cours de d&eacute;veloppement. Son code est modifi&eacute; en permanence ce qui le rend instable.

	<p>Merci de ne pas envoyer de rapport de bogue pour le moment

    <p>This demo site provides the following users. Log in as one of
    them to see the site through their eyes!

    <ul>
        <li>sysadmin - the SUPERUSER, who manages the system.</li>
        <li>admin - the Site Administrator, who manages the content.</li>
        <li>english - an English-speaking user.</li>
        <li>french - a French-speaking user.</li>
        <li>german - a German-speaking user.</li>
        <li>korean - a Korean-speaking user.</li>
    </ul>

    <p>All of these accounts use the password &quot;password&quot;.
    Log in as one of them, and check it out, or create your own
    account using the "Create Account" link to the right.
])

insert([doctable], [Table des docs], [Table des docs],
[
	|tabdocs|
])

insert([news], [|strproject| News], [|strprojectshort| News],
[
	|tabrecentnews|
])

insert([staff], [Staff], [],
[
    List the members of your project\'s staff here.
])

insert([contribute], [Contribuer &agrave; Lampadas], [Contribuer &agrave; Lampadas],
[
	En tant que membre de ce syst&egrave;me, vous b&eacute;n&eacute;ficiez du travail de plusieurs centaines d\'utilisateurs de Linux, qui ont b&eacute;n&eacute;volement contribu&eacute; &agrave; cr&eacute;er cette &eacute;norme biblioth&egrave;que &eacute;lectronique.

	<p>Nous sommes s&ucric;rs que vous souhaiteriez apporter votre pierre &agrave; l\'&eacute;difice aussi avons-nous con&ccedil;u Lampadas pour que vous puissiez ais&eacute;ment participer. Voici plusieurs fa&ccedil;ons d\'aider, class&eacute;es par ordre de difficult&eacute;:

	<ul>
	<li>Noter les documents

	<p>Chaque document est not&eacute;, sur une &eacute;chelle de 1 &agrave; 10, qui vous informe de l\'opinion qu\'en ont eu les autres lecteurs. Cette note nous permet de concentrer nos efforts sur l\'am&eacute;lioration des documents dont vous nous dites qu\'ils en ont le plus besoin.</li>

	<li>Signaler une erreur

	<p>Si vous trouvez une erreur dans un document, signalez-l&agrave;.

	</li>

	<li>Traduire un document
	<p>Les traducteurs sont toujours tr&egrave;s recherch&eacute;s, car notre
    but est d\'offrir notre documentation dans le plus grand nombre de langues
    possibles pour que tous puissent en profiter.
	</li>

	<li>Tranduire Lampadas
	<p>Le syst&egrave;me Lampadas peut &ecirc;tre localis&eacute; pour que chacun
    puisse l\'utiliser dans sa langue de pr&eacute;dilection.
	</li>
	
    <li>Ecrire un document
	<p>Si vous avez une comp&eacute;tence particuli&egrave;re, n\'h&eacute;sitez pas &agrave; &eacute;crire un nouveau document pour que nous le publions. Lampadas propose plusieurs outils pour vous faciliter cette t�che.
	</li>
	</ul>
])

insert([unmaintained], [Unmaintained Documents], [],
[
    |tabunmaintained|
])

insert([maint_wanted], [New Maintainer Wanted], [],
[
    |tabmaint_wanted|
])

insert([pending], [Pending Documents], [],
[
    |tabpending|
])

insert([wishlist], [Wishlist Documents], [],
[
    |tabwishlist|
])

insert([resources], [Other Resources], [],
[
    <ul>
        <li>Insert some resources for French authors.
    </ul>
])

insert([maillists], [Mailing Lists], [],
[
    List your project\'s mailing lists here.
])

insert([about], [A propos de |strproject|], [A propos de |strprojectshort|],
[
	Remplacez ce texte par la description de votre projet.
])

insert([lampadas], [A propos de Lampadas], [A propos de Lampadas],
[
    <p>This website is based on version |version| of the Lampadas
    Documentation Management System,
    a Free Software (GPL) platform developed by
    <a href="http://www.tldp.org">The Linux Documentation Project</a>.
    
    <p>Lampadas is a powerful, flexible platform designed to support
    large documentation projects such as the LDP.
    It provides an interactive environment for writing, managing,
    publishing and reading documentation.

    <p>Lampadas creates a collaborative community which
    includes authors, editors, technical experts, and readers all working
    together to produce documentation, and to share information with
    each other.

    <h1>Why Lampadas?</h1>

    <p>Fans of Frank Herbert\'s Dune series will recognize Lampadas
    as the name of the Bene Gesserit teaching planet, which plays a
    role in the final book,
    Chapterhouse: Dune.
    Before the planet can be destroyed by hordes of Honored Matres,
    Reverend Mother Lucilla orders the planet to share Other Memory,
    two by two then four by four, until all the students hold within
    them the composite knowledge and memories of the entire planet.
    After the planet is annihilated by the Honored Matres, the precious
    knowledge is carried back to the Bene Gesserit Chapterhouse by the
    lone holder of the precious cargo, Rebecca.

    <p>Herbert apparently took the name from the city of Lampadas,
    which was an ancient seat of learning and scholarship.
    Also, the word lampadas is the accusative form of the word
    "Torch" in ancient Greek.

    <p>In all of these senses, Lampadas seems an appropriate name for
    this project, which is created to facilitate sharing information
    from many people and many sources, and disseminating it widely to others.
])

insert([copyright], [Le Copyright], [Le Copyright],
[
	Copyright 2002 David Merrill.
])

insert([privacy], [Confidentialit&eacute;], [Confidentialit&eacute;],
[
	Confidentialit&eacute;
])

insert([sitemap], [Site Map], [],
[
    |tabsitemap|
])

insert([newuser], [New User], [],
[
    <p>To create a new user account, fill out this form.
    <p>
    <form name="newuser" action="adduser" method=GET>
        <table class="box">
            <tr>
                <td class="label">*Username</td>
                <td><input type=text name=username size=20></input></td>
            </tr>
            <tr>
                <td class="label">*Enter your email address.<br>Your password will be mailed to this address, so it must be valid.</td>
                <td><input type=text name=email size=20></input></td>
            </tr>
            <tr>
                <td class="label">First Name</td>
                <td><input type=text name=first_name size=20></input></td>
            </tr>
            <tr>
                <td class="label">Middle Name</td>
                <td><input type=text name=middle_name size=20></input></td>
            </tr>
            <tr>
                <td class="label">Surname</td>
                <td><input type=text name=surname size=20></input></td>
            </tr>
            <tr>
                <td colspan=2 align=center><input type=submit value="Create Account!"></td>
            </tr>
        </table
    </form>
    <p>*Required Fields
])

insert([topic], [View Topic], [View Topic],
[
    |tabsubtopics|
])

insert([subtopic], [View Subtopic], [],
[
    |tabsubtopic|
    |tabsubtopicdocs|
])

insert([editdoc], [M&eacute;ta-donn&eacute;es du doc], [M&eacute;ta-donn&eacute;es du doc],
[
	|tabeditdoc|
    |tabdocfiles|
    |tabdocusers|
    |tabdocversions|
    |tabdoctopics|
    |tabdocnotes|
    |tabdocerrors|
])

insert([404], [Introuvable], [Introuvable],
[
	Introuvable
])

insert([user_exists], [User Exists], [],
[
    <p>That username is already taken. Please select another username and try again.
])

insert([username_required], [Username Required] [],
[
    <p>Username is a required field. Please enter a username and try again.
])

insert([email_exists], [Email Exists], [],
[
    <p>That email address is already in the database.
    If you already have an account but have forgotten your password,
    you can have it <a href="mailpass">mailed</a> to you.
])

insert([account_created], [Account Created], [],
[
    <p>Your account has been created, and your password has been mailed to you.
    Please check your email.
])

insert([user], [Edit User Record], [Add User],
[
    |tabuser|
])

insert([logged_in], [Logged In], [],
[
    <p>You have been logged into the system.
])

insert([logged_out], [Logged Out], [],
[
    <p>You have been logged out of the system.
])

insert([type], [|type.name|], [],
[
    |tabtypedocs|
])

insert([cvslog], [CVS Log], [],
[
    |tabcvslog|
])

