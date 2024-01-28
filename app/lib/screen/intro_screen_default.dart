import 'package:flutter/material.dart';
import 'package:intro_slider/intro_slider.dart';
import 'package:samadhaan/screen/user_code_screen.dart';

class IntroScreenDefault extends StatefulWidget {
  const IntroScreenDefault({Key? key}) : super(key: key);

  @override
  IntroScreenDefaultState createState() => IntroScreenDefaultState();
}

class IntroScreenDefaultState extends State<IntroScreenDefault> {
  List<ContentConfig> listContentConfig = [];

  @override
  void initState() {
    super.initState();

    listContentConfig.add(
      const ContentConfig(
        title: "GRIEVANCE",
        description: "Raising Your Grievance just became easy... ",
        pathImage: "assets/images/complaint-1.png",
        backgroundColor: Colors.indigo,
      ),
    );
    listContentConfig.add(
      const ContentConfig(
        title: "RESPONSE",
        description:
            "Introducing AI Powered Grievance Redressal System launched by Government of India",
        pathImage: "assets/images/feedback-1.png",
        backgroundColor: Color(0xff203152),
      ),
    );
    listContentConfig.add(
      const ContentConfig(
        title: "SAMADHAAN",
        description: "Faster, Accurate and Easy",
        pathImage: "assets/images/satisfy-1.png",
        backgroundColor: Colors.black,
      ),
    );
  }

  // void onDonePress() {
  //   Navigator.of(context).push(
  //       MaterialPageRoute(builder: (context) => const GrievanceListScreen()));
  // }

  void onDonePress() {
    Navigator.of(context)
        .push(MaterialPageRoute(builder: (context) => const UserScreen()));
  }

  @override
  Widget build(BuildContext context) {
    return IntroSlider(
      key: UniqueKey(),
      listContentConfig: listContentConfig,
      onDonePress: onDonePress,
    );
  }
}
