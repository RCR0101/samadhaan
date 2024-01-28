import 'package:flutter/material.dart';

final ThemeData darkTheme = ThemeData(
  brightness: Brightness.dark,
  primaryColor: Colors.black,
  scaffoldBackgroundColor: Colors.black,
  appBarTheme: const AppBarTheme(
    color: Colors.indigo,
    elevation: 0,
  ),
  colorScheme: const ColorScheme.dark(
    primary: Colors.black,
    onPrimary: Colors.white,
    surface: Colors.black,
    onSurface: Colors.white,
  ),
  textTheme: const TextTheme(
      // Define text styles if needed
      ),
  // You can define other theme properties as needed
);
