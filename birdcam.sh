#!/bin/bash

stop_birdcam () {
	PID=$(lsof -t -i:5000)
	kill -9 "$PID"	
}

start_birdcam () {
	nohup /usr/bin/python3 /home/fluffyoctopus/birdcam/webserver.py &	
}

restart_if_necessary() {
	PID=$(lsof -t -i:5000)
	if [ -z "$PID" ];
	then
    		start_birdcam
	else
		exit
	fi

	exit
}


case "$1"
in
restart)
	stop_birdcam
	start_birdcam
	;;
stop) 
	stop_birdcam
	;;
start) 
	start_birdcam
	;;
alwaysOn)
	restart_if_necessary
	;;
esac
