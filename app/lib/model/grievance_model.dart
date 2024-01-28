class Grievance {
  String? id;
  String? orgCode;
  String? summary;
  String? details;
  String? status;
  String? userId;
  String? response;
  // String? responseDate;

  Grievance(
      {this.id,
      this.orgCode,
      this.summary,
      this.status,
      this.userId,
      this.details,
      this.response});

  factory Grievance.fromJson(Map<String, dynamic> json) {
    return Grievance(
      id: json['registration_no'],
      summary: json['title'],
      orgCode: json['org_code'],
      status: json['status'],
      userId: json['UserCode'],
      details: json['subject_content_text'],
      response: json['remarks_text'],
      // responseDate: json['resolution_date'],
    );
  }
}
