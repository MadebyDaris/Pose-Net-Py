import keypoints

PoseNetOutputStride = 32|16|8
PoseNetArchitecture = 'ResNet50'|'MobileNetV1'
PoseNetDecodingMethod = 'single-person'|'multi-person'
PoseNetQuantBytes = 1|2|4

MobileNetMultiplier = 0.50|0.75|1.0

Vector2D = {
  y: number,
  x: number
}

Part = {
  heatmapX: number,
  heatmapY: number,
  id: number
}

PartWithScore = {
  score: number,
  part: Part
}

Keypoint = {
  score: number,
  position: Vector2D,
  part: string
}

Pose = {
  keypoints: Keypoint,
  score: number,
}

PosenetInput =
    ImageData|HTMLImageElement|HTMLCanvasElement|HTMLVideoElement|tf.Tensor3D

ensorBuffer3D = tf.TensorBuffer<tf.Rank.R3>

Padding = {
  top: number;
  bottom: number;
  left: number;
  right: number;
}

InputResolution = number | {width: number, height: number}