#! /usr/bin/perl

print "Content-type: text/html\n";
print "Server-Software:",$ENV{'SERVER_NAME'},"\n";
print "Server-Port:",$ENV{'SERVER_PORT'},"\n";
print "Server-Protocol: ",$ENV{'SERVER_PROTOCOL'},"\n";
print "Content-Length:",$ENV{'CONTENT_LENGTH'},"\n";
print "Remote-Addr: ",$ENV{'REMOTE_ADDR'},"\n";
print "\n\n";

print "<html><head><title>Simple CGI</title></head>";
print "<h1> My Simple CGI </h1><body><div id='project_links'>";
print "<li><a href = 'http://github.com/mh122354/VR-Frogger'>VR Frogger Game";
print "</a></li><li><a href = 'http://github.com/mh122354/Space-Shooter'>Space";
print "Shooter Game</a></li><li><a href='http://github.com/mh122354/7MinuteWorkout'>7 Minute Workout";
print "</a></li></ul></div>";
print"</body></html>";
