帮我写一个基于fastAPI的yolo检测项目。要求如下：

1. yolo采用ultralytics库的yolov11s，预训练模型即可。
2. 项目主要分为图像上传，目标检测，结果保存，结果查询四个主要方法。
3. 图像上传后先进行目标检测，检测完后，将原始图像和预测结果图像，上传到minIO OSS中，并将图像url地址保存进数据库，
4. 同时将预测结果如分类，框选坐标，置信度等同步保存在数据库中。
5. 数据库采用mysql
6. 要有一个查询方法可以查询历史结果。
7. 使用pydantic构建pojo。
8. 使用sqlalchemy和aiomysql 
9. 要有合适的项目结构类似spring-boot项目那样。
10. 从头开始讲解，包括minIO安装，conda环境搭建
11. 添加任务状态（pending/processing/done）
