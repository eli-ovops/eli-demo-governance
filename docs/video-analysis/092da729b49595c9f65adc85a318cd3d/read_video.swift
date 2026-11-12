import Foundation
import AVFoundation
import Vision
import AppKit

let source = CommandLine.arguments[1]
let out = CommandLine.arguments[2]
let asset = AVURLAsset(url: URL(fileURLWithPath: source))
let duration = CMTimeGetSeconds(asset.duration)
let tracks = asset.tracks.map { ["type": $0.mediaType.rawValue, "duration": CMTimeGetSeconds($0.timeRange.duration), "width": Double($0.naturalSize.width), "height": Double($0.naturalSize.height)] as [String: Any] }
let meta: [String: Any] = ["duration":duration, "tracks":tracks, "source":source]
try JSONSerialization.data(withJSONObject: meta, options:.prettyPrinted).write(to:URL(fileURLWithPath:out+"/metadata.json"))
print(String(data:try JSONSerialization.data(withJSONObject:meta),encoding:.utf8)!)
let gen = AVAssetImageGenerator(asset:asset)
gen.appliesPreferredTrackTransform = true
gen.maximumSize = CGSize(width:1280,height:1280)
gen.requestedTimeToleranceBefore = .zero
gen.requestedTimeToleranceAfter = .zero
var rows = [[String:Any]]()
let interval = Double(CommandLine.arguments.count > 3 ? CommandLine.arguments[3] : "2")!
for t in stride(from:0.0,to:duration,by:interval) {
  autoreleasepool {
    do {
      let cg = try gen.copyCGImage(at:CMTime(seconds:t,preferredTimescale:600), actualTime:nil)
      let req = VNRecognizeTextRequest()
      req.recognitionLanguages = ["zh-Hans","en-US"]
      req.recognitionLevel = .accurate
      try VNImageRequestHandler(cgImage:cg).perform([req])
      let texts = (req.results ?? []).map { $0.topCandidates(1).first?.string ?? "" }
      rows.append(["time":t,"text":texts])
      if t == 0 || Int(t) % 120 == 0 {
        let rep = NSBitmapImageRep(cgImage:cg)
        try rep.representation(using:.jpeg,properties:[.compressionFactor:0.75])!.write(to:URL(fileURLWithPath:out+"/frame_\(Int(t)).jpg"))
        print("progress \(t)/\(duration)")
        fflush(stdout)
      }
    } catch { rows.append(["time":t,"error":String(describing:error)]) }
  }
}
try JSONSerialization.data(withJSONObject:rows,options:[.prettyPrinted,.sortedKeys]).write(to:URL(fileURLWithPath:out+"/ocr.json"))
print("finished \(rows.count) frames")
