if __name__ == '__main__':
    from deepl_translator import CustomDeepLCLI
    
    if 'fetch' in sys.argv:
        test_client = CustomDeepLCLI(
            "en", "ru",
            headless=False,
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        )
        if not os.path.exists('pages'):
            os.mkdir('pages')

        if not os.path.exists('pages/translated'):
            os.mkdir('pages/translated')

        test_client.loop.run_until_complete(test_client.start_browser())

        for chapter in os.listdir('target'):
            translated_chapter_buf = []
            if chapter.endswith(".md"):
                print(chapter)
                
                reader = open(f'target/{chapter}', 'r', encoding='utf')
                writer = open(f'pages/translated/{chapter}', 'w', encoding='utf')
                for text_block in str(reader.read()).split('\n'):
                    if not text_block or text_block.startswith('`'):
                        translated_chapter_buf.append(
                            text_block
                        )
                    else:
                        translated_chapter_buf.append(
                            test_client.translate(
                                text_block
                            )
                        )
                print(chapter, "translated")
                writer.write("\n".join(translated_chapter_buf))
                writer.close()
                reader.close()
