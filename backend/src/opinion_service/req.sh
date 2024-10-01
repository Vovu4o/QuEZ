curl -i -X 'POST' \
  'http://localhost:8888/api/upload_opinion/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/home/QuEZ/backend/src/opinion_service/test_sentences/sentences.csv;type=application/csv'
