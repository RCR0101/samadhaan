import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:http/http.dart' as http;
import 'package:samadhaan/common/constant.dart';
import 'package:samadhaan/model/grievance_model.dart';
import 'package:samadhaan/provider/user_code_provider.dart';

class PostGrievance extends ConsumerWidget {
  const PostGrievance({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
        appBar: AppBar(title: const Text('Post Grievance')),
        body: GrievanceForm());
  }
}

class GrievanceForm extends ConsumerWidget {
  GrievanceForm({super.key});
  final titleController = TextEditingController();
  final detailsController = TextEditingController();

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    var screenSize = MediaQuery.of(context).size;
    return Center(
      child: SizedBox(
        height: screenSize.height * .8,
        width: screenSize.width * .8,
        child: Padding(
          padding: const EdgeInsets.all(4.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextFormField(
                decoration:
                    const InputDecoration(labelText: 'Please provide summary'),
                controller: titleController,
              ),
              // const SizedBox(height: 20),
              TextFormField(
                decoration: const InputDecoration(
                    labelText: 'Please provide details that will help us'),
                maxLines: 15,
                controller: detailsController,
              ),
              const Spacer(),
              ElevatedButton(
                onPressed: () => handleSubmission(
                    context,
                    ref,
                    Grievance(
                        summary: titleController.text,
                        details: detailsController.text)),
                child: const Text('Submit Grievance'),
              )
            ],
          ),
        ),
      ),
    );
  }

  void handleSubmission(
      BuildContext context, WidgetRef ref, Grievance grievance) async {
    bool isSuccess = await submitGrievance(ref, grievance);
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text(isSuccess ? 'Success' : 'Failure')),
    );

    if (isSuccess) {
      Future.delayed(const Duration(seconds: 10), () {
        Navigator.of(context).pop();
      });
    }
  }

  Future<bool> submitGrievance(WidgetRef ref, Grievance grievance) async {
    final userCode = ref.watch(userCodeProvider);
    final response = await http.post(
      Uri.parse('${API_URL_BASE}Complaints'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'id': grievance.id,
        'title': grievance.summary,
        'subject_content_text': grievance.details,
        'status': "New",
        'UserCode': userCode,
      }),
    );

    return response.statusCode == 201 || response.statusCode == 200;
  }
}
