include .env

run-detect:
	cd yolov5 && \
	python detect.py --source $(YOLO_SOURCE) --conf $(YOLO_CONF) --weights $(YOLO_WEIGHTS) --name $(YOLO_NAME)
run-detect-txt:
	cd yolov5 && \
	python detect.py --source $(YOLO_SOURCE) --conf $(YOLO_CONF) --weights $(YOLO_WEIGHTS) --name $(YOLO_NAME) --save-txt --classes 2
run-train:
	cd yolov5 && \
	python train.py --data $(YOLO_TRAIN_DATA) --conf $(YOLO_TRAIN_CONF) --weights $(YOLO_TRAIN_WEIGHTS) --batch-size $(YOLO_TRAIN_BATCH_SIZE) --img $(YOLO_TRAIN_IMG)