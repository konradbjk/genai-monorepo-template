import { GitHubButton } from '@packages/ui'
import Link from 'next/link';
import { useTranslations } from 'next-intl';

export default function Index() {
  const t = useTranslations('HomePage');
  return (
    <div className="min-h-screen bg-gradient-to-b from-white to-gray-100">
      <div className="container mx-auto px-4 py-16">
        <header className="text-center mb-16">
          <h1 className="text-4xl font-bold mb-4">Konrad Bujak</h1>
          <p className="text-xl text-gray-600 mb-8">CTO @ BuyerMind | Founder @ CEE AI Hub</p>

          <div className="flex flex-wrap justify-center gap-4">
            <Link href={"https://www.konradbujak.com"} target="_blank" rel="noopener noreferrer"
              >
                Visit My Website
                </Link>
          </div>
        </header>

        <main className="max-w-3xl mx-auto">
          <section className="bg-white rounded-lg shadow-lg p-8 mb-8">
            <h2 className="text-2xl font-semibold mb-4">{t("sectionTitles.aboutMe")}</h2>
            <p className="mb-4 text-gray-700">
            {t("about")}
            </p>
            <p className="text-gray-700">
              {t("passion")}
            </p>
          </section>

          <section className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-semibold mb-4">{t("sectionTitles.buyerMindPlatform")}</h2>
            <p className="mb-4 text-gray-700">
              {t("AbutBuyerMind")}
            </p>
            <div className="mt-6">
              <GitHubButton label='My GitHub' href='https://github.com/konradbjk'/>
            </div>
          </section>
        </main>

        <footer className="mt-16 text-center text-gray-500">
          <p>© {new Date().getFullYear()} Konrad Bujak. All rights reserved.</p>
        </footer>
      </div>
    </div>
  );
}
