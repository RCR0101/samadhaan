import torch
from torch.utils.data import DataLoader, TensorDataset, random_split
from transformers import BertForSequenceClassification, AdamW
from torch.nn import CrossEntropyLoss

# Define the label map
urgency_map = {
    "low": 0,
    "normal": 1,
    "med": 2,
    "high": 3,
    "urgent": 4,
    "critical" : 5
}

texts = [
    "urgent system failure, please respond immediately",
    "routine checkup required, no immediate action needed",
    "high priority: server downtime reported",
    "customer inquiry, please respond within standard timeframes",
    "critical performance issue affecting multiple users",
    "normal maintenance scheduled for next week",
    "urgent: security breach detected in the database",
    "feedback on services, not urgent",
    "software update required, medium priority",
    "low priority: update documentation",
    "server performance optimization, high importance",
    "general question about account settings",
    "urgent assistance required for system outage",
    "non-critical bug found in the application",
    "high-priority customer complaint, immediate attention needed",
    "reminder: team meeting tomorrow",
    "urgent: compliance issue needs to be addressed",
    "normal query regarding billing",
    "critical: data loss incident reported",
    "feedback request on recent update, not urgent"
]

lbls = [
    "urgent",  # urgent system failure
    "low",     # routine checkup
    "high",    # high priority server downtime
    "normal",  # customer inquiry
    "critical",# critical performance issue
    "normal",  # normal maintenance
    "urgent",  # urgent security breach
    "low",     # feedback, not urgent
    "med",     # software update, medium priority
    "low",     # low priority documentation update
    "high",    # high importance server optimization
    "normal",  # general account question
    "urgent",  # urgent system outage
    "low",     # non-critical bug
    "high",    # high-priority customer complaint
    "low",     # meeting reminder
    "urgent",  # urgent compliance issue
    "normal",  # normal billing query
    "critical",# critical data loss
    "low"      # feedback request, not urgent
]

def create_severity_model():
    # Convert labels to numerical format
    labels = torch.tensor([urgency_map[label] for label in lbls])
    dataset = TensorDataset(torch.tensor(list(texts)), labels)

    # Split the dataset
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, _ = random_split(dataset, [train_size, val_size])

    # Load the model and initialize optimizer and loss function
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(urgency_map))
    optimizer = AdamW(model.parameters(), lr=1e-5)
    criterion = CrossEntropyLoss()
    epochs=3
    batch_size=2
    # Training loop
    model.train()
    for epoch in range(epochs):
        for batch in DataLoader(train_dataset, batch_size=batch_size, shuffle=True):
            input_ids, batch_labels = batch
            model.zero_grad()
            outputs = model(input_ids)
            loss = criterion(outputs.logits, batch_labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch} complete, Loss: {loss.item()}")

    # Prediction


    return model

def calculate_severity(model, new_complaint_text):
    model.eval()
    with torch.no_grad():
        inputs = torch.tensor([new_complaint_text])
        outputs = model(inputs)
    logits = outputs.logits
    predicted_urgency_index = torch.argmax(logits, dim=1).item()
    predicted_urgency = [k for k, v in urgency_map.items() if v == predicted_urgency_index][0]
    return predicted_urgency



sev_model = create_severity_model()
# Test the pipeline with a new complaint
# new_complaint_text = "Your complaint text here"
new_complaint_text  = "My INDIAN Passport number: X7X3X4X0 \r\n\r\nMy Immigration Newzealand client number: X3X2X0X4 \r\n\r\n\r\n\r\n\r\n\r\n\r\nI Danapuneni Sreekanth Rao,I paid fee to the college,and I paid taxes to New-Zealand Government in 2009 year.without provided any services how they took my tution fee?all these things because of New-Zealand Government iam facing health problems.why they took my tution fee,without provided anything.due to loss of my 11years I should get permanent residency and compensation of New-Zealand dollars 913336 NZD.all my friends are in good position in jobs.iam mentally faced lot of problems because of New-Zealand Government.So I should get permanent residency and compensation of New-Zealand dollars 913336 NZD from Indian Government. \r\n\r\n\r\n\r\n\r\n\r\nBank Details: \r\nACCOUNT NAME: Sreekanth Rao Danapuneni \r\n\r\nACCOUNT NO: X2X8X8X9X8X \r\n\r\nIFSC CODE: X-X-X-X-X \r\n\r\nBANK: STATE BANK OF INDIA \r\n\r\nBRANCH:MANTHANI \r\nSTATE. : TELANGANA \r\nCOUNTRY :. INDIA \r\n\r\n\r\nThanks and regards \r\n----------------------- \r\nDanapuneni Sreekanth Rao"
predicted_urgency = calculate_severity(sev_model, new_complaint_text)
print(f"The text '{new_complaint_text}' is predicted as: {predicted_urgency}")