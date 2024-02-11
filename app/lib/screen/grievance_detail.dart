import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:samadhaan/model/grievance_model.dart';
import 'package:samadhaan/provider/grievance_provider.dart';

class GrievanceDetailScreen extends ConsumerWidget {
  const GrievanceDetailScreen({super.key, required this.id});
  final String id;
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
        appBar: AppBar(title: const Text('Samadhaan')),
        body: Center(
            child: Padding(
                padding: const EdgeInsets.all(4.0),
                child: GrievanceWidget(id: id))));
  }
}

class GrievanceWidget extends ConsumerWidget {
  const GrievanceWidget({super.key, required this.id});
  final String id;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final grievanceData = ref.watch(grievanceProvider(id));

    return grievanceData.when(
      data: (grievance) => showCard(grievance, ref),
      loading: () => const CircularProgressIndicator(),
      error: (e, _) => Text('Error: $e'),
    );
  }

  Widget showCard(Grievance grievance, WidgetRef ref) { // Add WidgetRef ref as a parameter to access the ref.refresh method
  String sts = grievance.status == "2" ? "In Progress" : "Resolved";

  return Container(
    decoration: BoxDecoration(
      boxShadow: [
        BoxShadow(
          color: Colors.grey.withOpacity(0.5),
          spreadRadius: 2,
          blurRadius: 7,
          offset: const Offset(0, 5), // changes position of shadow
        ),
      ],
    ),
    child: Card(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('ID: ${grievance.id}'),
          Text('Summary: ${grievance.summary}'),
          Text('Status: $sts'),
          Text('User Code: ${grievance.userId}'),
          Expanded(
              child: Text('Grievance Raised:\n\n ${grievance.details}')),
          Expanded(child: Text('\n\nResponse: \n\n${grievance.response}')),
          // Add a button to refresh the data
          TextButton(
            onPressed: () => ref.refresh(grievanceProvider(id)), // Force refresh the grievance data
            child: const Text('Refresh'),
          ),
          // Text(
          //     'Response Date: ${grievance.responseDate != null ? formatDateString(grievance.responseDate!) : 'N/A'}'),
        ],
      ),
    ),
  );
}


  // Widget showCard(Grievance grievance) {
  //   String sts = grievance.status == "2" ? "In Progress" : "Resolved";

  //   return Container(
  //       decoration: BoxDecoration(
  //         boxShadow: [
  //           BoxShadow(
  //             color: Colors.grey.withOpacity(0.5),
  //             spreadRadius: 2,
  //             blurRadius: 7,
  //             offset: const Offset(0, 5), // changes position of shadow
  //           ),
  //         ],
  //       ),
  //       child: Card(
  //         child: Column(
  //           crossAxisAlignment: CrossAxisAlignment.start,
  //           children: [
  //             Text('ID: ${grievance.id}'),
  //             Text('Summary: ${grievance.summary}'),
  //             Text('Status: $sts'),
  //             Text('User Code: ${grievance.userId}'),
  //             Expanded(
  //                 child: Text('Grievance Raised:\n\n ${grievance.details}')),
  //             Expanded(child: Text('\n\nResponse: \n\n${grievance.response}')),
  //             // Text(
  //             //     'Response Date: ${grievance.responseDate != null ? formatDateString(grievance.responseDate!) : 'N/A'}'),
  //           ],
  //         ),
  //       ));
  // }
}
