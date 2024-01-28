import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:samadhaan/model/grievance_model.dart';
import 'package:samadhaan/provider/grievance_provider.dart';
import 'package:samadhaan/screen/grievance_detail.dart';
import 'package:samadhaan/screen/post_grievance.dart';

class GrievanceListScreen extends ConsumerWidget {
  const GrievanceListScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
        appBar: AppBar(title: const Text('Samadhaan')),
        body: const Center(
            child: Padding(
                padding: EdgeInsets.all(4.0), child: GrievanceListView())));
  }
}

class GrievanceListView extends ConsumerWidget {
  const GrievanceListView({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final asyncGrievances = ref.watch(grievanceListProvider);

    return Scaffold(
      body: RefreshIndicator(
        onRefresh: () => ref.refresh(grievanceListProvider.future),
        child: asyncGrievances.when(
          data: (grievances) {
            if (grievances.isEmpty) {
              return const Center(
                child: Text('No grievances registered'),
              );
            } else {
              return ListView.builder(
                itemCount: grievances.length,
                itemBuilder: (context, index) {
                  final grievance = grievances[index];
                  return showGrievance(grievance, context);
                },
              );
            }
          },
          loading: () => const CircularProgressIndicator(),
          error: (err, stack) => Text('Error: $err'),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.of(context).push(
            MaterialPageRoute(builder: (context) => const PostGrievance()),
          );
        },
        tooltip: 'Post New Grievance',
        child: const Icon(Icons.add),
      ),
    );
  }

  ListTile showGrievance(Grievance grievance, BuildContext context) {
    Color textColor = Colors.black; // Default color
    String txt = "";
    if (grievance.status == '2') {
      txt = "In Progress";
      textColor = Colors.orange;
    } else if (grievance.status == '3') {
      txt = "Resolved";
      textColor = Colors.green;
    }

    return ListTile(
      title: Text(
        grievance.id!,
        style: TextStyle(color: textColor), // Apply the color here
      ),
      subtitle: Text(
        'Status: $txt',
        style: TextStyle(color: textColor), // Apply the color here
      ),
      onTap: () {
        Navigator.of(context).push(
          MaterialPageRoute(
            builder: (context) => GrievanceDetailScreen(id: grievance.id!),
          ),
        );
      },
    );
  }
}
