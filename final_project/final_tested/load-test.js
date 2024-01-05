import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  http.get('http://34.41.3.206/');
  sleep(1);
}

