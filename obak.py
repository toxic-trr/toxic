import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))