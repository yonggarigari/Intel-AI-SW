# Homework03
Smart factory 불량 분류모델 training 결과

## Dataset 구조
```
(.otx) yong@yong:~/workspace/otx-defect/classfication-mobile$ ds_count ./splitted_dataset/ 2
./splitted_dataset/./:	455
./splitted_dataset/./val:	91
./splitted_dataset/./val/nok:	46
./splitted_dataset/./val/ok:	45
./splitted_dataset/./train:	364
./splitted_dataset/./train/nok:	185
./splitted_dataset/./train/ok:	179

```

## Training 결과
|Classification model|Accuracy|FPS|Training time|Batch size|Learning rate|Other hyper-prams|
|----|----|----|----|----|----|----|
|EfficientNet-V2-S|1.000|73.89|0:01:00.854022|32|0.0058
|EfficientNet-B0|1.000|160.28|0:00:23.564293|32|0.0058
|DeiT-Tiny|1.000|49.83|0:00:16.967628|32|0.0058
|MobileNet-V3-large-1x|1.000|248.76|0:00:12.951682|32|0.0058


## FPS 측정 방법
```
 --------------------------- Step 6. Create infer request and do inference synchronously -----------------------------
    log.info('Starting inference in synchronous mode')
    prev_time = time.time()
    results = compiled_model.infer_new_request({0: input_tensor})
    
 --------------------------- Step 7. Process output ------------------------------------------------------------------
    predictions = next(iter(results.values()))

    sec = time.time() - prev_time
    fps = 1/(sec)
    log.info(f"FPS: {fps:.2f}")
```
