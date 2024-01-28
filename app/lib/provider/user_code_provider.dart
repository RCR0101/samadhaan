import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

final userCodeProvider =
    StateNotifierProvider<UserCodeNotifier, String?>((ref) {
  return UserCodeNotifier();
});

class UserCodeNotifier extends StateNotifier<String?> {
  UserCodeNotifier() : super(null) {
    _loadUserCode();
  }

  Future<void> _loadUserCode() async {
    final prefs = await SharedPreferences.getInstance();
    state = prefs.getString('userCode');
  }

  Future<void> setUserCode(String? code) async {
    final prefs = await SharedPreferences.getInstance();
    if (code == null) {
      await prefs.remove('userCode');
    } else {
      await prefs.setString('userCode', code);
    }
    state = code;
  }
}
