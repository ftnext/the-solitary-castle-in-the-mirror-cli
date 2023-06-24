FROM python:3.11-bookworm as builder
RUN python -m pip install --no-cache-dir kojo-fan-art

FROM python:3.11-slim-bookworm
COPY --from=builder /usr/local/bin/kojo-day /usr/local/bin/kojo-day
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
ENV TZ='Asia/Tokyo'
ENTRYPOINT [ "kojo-day" ]
CMD [ "kokoro", "aki", "fuka", "rion", "subaru", "masamune", "ureshino" ]
