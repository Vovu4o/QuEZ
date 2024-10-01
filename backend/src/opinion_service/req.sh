curl -i -X 'POST' http://localhost:8888/upload_opinion/ -H "Content-Type: application/json" -H 'Content-Type: multipart/form-data' --data-binary "file=@/home/QuEZ/backend/src/opinion_service/sentences.csv;type=application/csv";

