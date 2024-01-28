import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:samadhaan/screen/intro_screen_default.dart';
import 'package:samadhaan/style/locale.dart';

void main() {
  runApp(
    const ProviderScope(
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      localizationsDelegates: const [
        AppLocalizationsDelegate(),
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [
        Locale('hi', 'IN'), // Hindi
        // Add other locales if needed
      ],
      title: 'Samadhaan',
      debugShowCheckedModeBanner: false,
      themeMode: ThemeMode.dark,
      theme: ThemeData(),
      darkTheme: ThemeData(
        brightness: Brightness.dark,
        primarySwatch: Colors.grey,
        // Customize other theme properties as needed
      ),
      // darkTheme: darkTheme,
      home: const IntroScreenDefault(),
      //  const GrievanceListScreen(),
      // ChatScreen(),
      // UserInfoScreen(),
    );
  }
}
