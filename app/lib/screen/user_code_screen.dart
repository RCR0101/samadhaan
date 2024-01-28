import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:samadhaan/provider/user_code_provider.dart';
import 'package:samadhaan/screen/grievance_list_view.dart';

class UserScreen extends ConsumerWidget {
  const UserScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
        appBar: AppBar(title: const Text('Samadhaan')),
        body: Center(
            child: Padding(
                padding: const EdgeInsets.all(4.0), child: UserCodeWidget())));
  }
}

class UserCodeWidget extends ConsumerWidget {
  UserCodeWidget({super.key});
  final codeController = TextEditingController();
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // final userCode = ref.watch(userCodeProvider);

    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: TextFormField(
            // initialValue: userCode,
            controller: codeController,
            decoration: const InputDecoration(
              labelText: 'Enter User Code',
              border: OutlineInputBorder(),
            ),
            // onChanged: (value) {
            //   ref.read(userCodeProvider.notifier).setUserCode(value);
            // },
          ),
        ),
        ElevatedButton(
          onPressed: () {
            onDonePress(ref, context);
          },
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.green, // Background color
          ),
          child: const Text('Continue to Grievance'),
        ),
        const Spacer(),
        ElevatedButton(
          onPressed: () {
            ref.read(userCodeProvider.notifier).setUserCode(null);
          },
          child: const Text('Reset User Code'),
        ),
      ],
    );
  }

  void onDonePress(WidgetRef ref, BuildContext context) {
    ref.read(userCodeProvider.notifier).setUserCode(codeController.text);
    Navigator.of(context).push(
        MaterialPageRoute(builder: (context) => const GrievanceListScreen()));
  }
}
