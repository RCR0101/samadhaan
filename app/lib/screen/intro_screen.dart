// import 'package:flutter/material.dart';
// import 'package:intro_slider/intro_slider.dart';
// import 'package:samadhaan/screen/grievance_list_view.dart';
// import 'package:samadhaan/screen/intro_screen_default.dart';

// class IntroScreenDefaultState extends State<IntroScreenDefault> {
//   List<ContentConfig> listContentConfig = [];

//   @override
//   void initState() {
//     super.initState();

//     listContentConfig.add(
//       const ContentConfig(
//         title: "ERASER",
//         description:
//             "Allow miles wound place the leave had. To sitting subject no improve studied limited",
//         pathImage: "images/photo_eraser.png",
//         backgroundColor: Color(0xfff5a623),
//       ),
//     );
//     listContentConfig.add(
//       const ContentConfig(
//         title: "PENCIL",
//         description:
//             "Ye indulgence unreserved connection alteration appearance",
//         pathImage: "images/photo_pencil.png",
//         backgroundColor: Color(0xff203152),
//       ),
//     );
//     listContentConfig.add(
//       const ContentConfig(
//         title: "RULER",
//         description:
//             "Much evil soon high in hope do view. Out may few northward believing attempted. Yet timed being songs marry one defer men our. Although finished blessing do of",
//         pathImage: "images/photo_ruler.png",
//         backgroundColor: Color(0xff9932CC),
//       ),
//     );
//   }

//   void onDonePress() {
//     Navigator.of(context).push(
//         MaterialPageRoute(builder: (context) => const GrievanceListScreen()));
//   }

//   @override
//   Widget build(BuildContext context) {
//     return IntroSlider(
//       key: UniqueKey(),
//       listContentConfig: listContentConfig,
//       onDonePress: onDonePress,
//     );
//   }
// }
