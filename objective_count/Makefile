include .env

run-detect:
	cd yolov5 && \
	python detect.py --source $(YOLO_SOURCE) --conf $(YOLO_CONF) --weights $(YOLO_WEIGHTS) --name $(YOLO_NAME) 