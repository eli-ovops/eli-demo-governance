import Foundation
import AVFoundation
import AppKit
let asset = AVURLAsset(url:URL(fileURLWithPath:CommandLine.arguments[1]))
let gen = AVAssetImageGenerator(asset:asset)
gen.appliesPreferredTrackTransform = true
gen.requestedTimeToleranceBefore = .zero
gen.requestedTimeToleranceAfter = .zero
for t in [15,19,37,125,155,160,317,520,619,813,1296,1555,1567,1842,2101,2193,2513,2584,3260,3724,3918,4350,4895,5011,5201,5320,5442,5585,5708,5925] {
  let cg = try gen.copyCGImage(at:CMTime(seconds:Double(t),preferredTimescale:600),actualTime:nil)
  let rep = NSBitmapImageRep(cgImage:cg)
  try rep.representation(using:.jpeg,properties:[.compressionFactor:0.85])!.write(to:URL(fileURLWithPath:CommandLine.arguments[2]+"/review_\(t).jpg"))
}
