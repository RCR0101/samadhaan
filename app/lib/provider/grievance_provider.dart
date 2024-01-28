import 'dart:convert';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:http/http.dart' as http;
import 'package:samadhaan/common/constant.dart';
import 'package:samadhaan/model/grievance_model.dart';
import 'package:samadhaan/provider/user_code_provider.dart';

final grievanceListProvider = FutureProvider<List<Grievance>>((ref) async {
  final userCode = ref.watch(userCodeProvider);

  final response =
      await http.get(Uri.parse('${API_URL_BASE}Complaints/User/$userCode'));

  if (response.statusCode == 200) {
    List<dynamic> grievancesJson = jsonDecode(response.body);
    return grievancesJson.map((json) => Grievance.fromJson(json)).toList();
  } else {
    // throw Exception('Failed to load grievances');
    return <Grievance>[];
  }
});

// 2. Create a Provider for fetching data
final grievanceProvider =
    FutureProvider.family<Grievance, String>((ref, id) async {
  final response = await http.get(Uri.parse('${API_URL_BASE}Complaints/$id'));
  if (response.statusCode == 200) {
    return Grievance.fromJson(json.decode(response.body));
  } else {
    throw Exception('Failed to load data');
  }
});
