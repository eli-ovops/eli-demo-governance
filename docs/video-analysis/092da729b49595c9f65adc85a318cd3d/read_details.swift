import Foundation
import AVFoundation
import AppKit
let asset = AVURLAsset(url:URL(fileURLWithPath:CommandLine.arguments[1]))
let gen = AVAssetImageGenerator(asset:asset)
gen.appliesPreferredTrackTransform = true
gen.requestedTimeToleranceBefore = .zero
gen.requestedTimeToleranceAfter = .zero
for t in [676,710,832,1752,2060,2510,2542,4664,5952] {
  let cg = try gen.copyCGImage(at:CMTime(seconds:Double(t),preferredTimescale:600),actualTime:nil)
  let rep = NSBitmapImageRep(cgImage:cg)
  try rep.representation(using:.jpeg,properties:[.compressionFactor:0.85])!.write(to:URL(fileURLWithPath:CommandLine.arguments[2]+"/detail_\(t).jpg"))
}
