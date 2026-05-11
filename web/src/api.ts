import { getToken } from './auth';

const API_BASE_URL: string = (import.meta.env.VITE_API_BASE_URL as string | undefined) ?? '';

export type ApiInit = Omit<RequestInit, 'body'> & {
  body?: unknown;
};

export class ApiError extends Error {
  constructor(
    public readonly status: number,
    public readonly responseBody: string,
  ) {
    super(`API ${status}: ${responseBody}`);
    this.name = 'ApiError';
  }
}

export async function apiFetch<T>(path: string, init: ApiInit = {}): Promise<T> {
  const { body, headers, ...rest } = init;
  const finalHeaders = new Headers(headers);

  if (body !== undefined && !finalHeaders.has('Content-Type')) {
    finalHeaders.set('Content-Type', 'application/json');
  }

  const token = getToken();
  if (token !== null) {
    finalHeaders.set('Authorization', `Bearer ${token}`);
  }

  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...rest,
    headers: finalHeaders,
    body: body === undefined ? undefined : JSON.stringify(body),
  });

  if (!response.ok) {
    const text = await response.text().catch(() => '');
    throw new ApiError(response.status, text);
  }

  if (response.status === 204) {
    return undefined as T;
  }
  return (await response.json()) as T;
}
